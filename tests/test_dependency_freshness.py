"""Contract tests for the dependency freshness check.

The check is only useful if a red line means "someone has to look". Two things
can make that false: a false alarm that fires every month until people stop
reading the report, and a silencing move that hides a real gap. These tests pin
both edges -- the declared-precision comparison, and the two documented exits
(hold and deferral) with the deferral expiring by itself.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_dependency_freshness as checker  # noqa: E402


def test_comparison_uses_the_precision_the_declaration_states() -> None:
    # `>=7` says nothing about the minor, so 7.4.0 must not be a monthly alarm.
    assert not checker.is_newer_version("7.4.0", "7")
    assert checker.is_newer_version("8.0.0", "7")
    assert checker.is_newer_version("7.4.0", "7.3")
    assert not checker.is_newer_version("7.3.2", "7.3")


def test_prerelease_suffix_does_not_count_as_newer() -> None:
    assert not checker.is_newer_version("7.0.0rc1", "7.0.0")


def test_hold_marker_is_read_off_the_declaring_line() -> None:
    packages = checker.parse_requirements(
        "pytest>=8.3  # freshness-hold: pytest 9 requires Python 3.10, CI still tests 3.9\n"
        "ruff>=0.16\n",
        "requirements-dev.txt",
    )

    holds = {package["name"]: package["hold"] for package in packages}
    assert holds["ruff"] == ""
    assert holds["pytest"].startswith("pytest 9 requires Python 3.10")


def test_a_held_floor_is_reported_but_does_not_ask_for_work(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(checker, "fetch_pypi_version", lambda name: "9.1.0")
    packages = checker.parse_requirements(
        "pytest>=8.3  # freshness-hold: CI still tests 3.9\n", "requirements-dev.txt"
    )

    rows = checker.collect_status(packages, deferrals={})

    assert rows[0]["outdated"] is True
    assert checker.needs_review(rows[0]) is False
    assert "HELD: CI still tests 3.9" in checker.render_markdown(rows)


def test_a_live_deferral_covers_the_row_and_says_what_it_was_reviewed_against(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(checker, "fetch_pypi_version", lambda name: "9.1.0")
    packages = checker.parse_requirements("pytest>=8.3\n", "requirements-dev.txt")

    rows = checker.collect_status(
        packages, deferrals={"pytest": ("9.1", "reviewed 2026-08; wait for the 9.x line to settle")}
    )

    assert checker.needs_review(rows[0]) is False
    assert "DEFERRED at 9.1.0" in checker.render_markdown(rows)


def test_a_deferral_expires_once_pypi_moves_past_the_reviewed_release(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """This is the whole point of `deferredLatest`: it cannot become a mute button."""
    monkeypatch.setattr(checker, "fetch_pypi_version", lambda name: "10.0.0")
    packages = checker.parse_requirements("pytest>=8.3\n", "requirements-dev.txt")

    rows = checker.collect_status(packages, deferrals={"pytest": ("9.1", "not this month")})

    assert checker.needs_review(rows[0]) is True
    assert "REVIEW UPDATE" in checker.render_markdown(rows)


def test_deferral_without_a_reviewed_release_is_ignored(tmp_path: Path) -> None:
    path = tmp_path / "dependency-deferrals.json"
    path.write_text(
        json.dumps(
            {
                "deferrals": {
                    "kept": {"deferredLatest": "9.1", "reason": "reviewed, not now"},
                    "no-release": {"reason": "reviewed, not now"},
                    "no-reason": {"deferredLatest": "9.1"},
                }
            }
        ),
        encoding="utf-8",
    )

    assert checker.load_deferrals(path) == {"kept": ("9.1", "reviewed, not now")}


def test_missing_deferrals_file_is_not_an_error(tmp_path: Path) -> None:
    assert checker.load_deferrals(tmp_path / "nope.json") == {}


def test_report_names_both_exits_so_the_next_person_does_not_invent_a_third() -> None:
    report = checker.render_markdown([])

    assert "freshness-hold:" in report
    assert "dependency-deferrals.json" in report
    assert "mute button" in report


def test_strict_run_with_no_declared_dependencies_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """An empty table renders CHECK FAILED; --strict must not exit 0 on it."""
    monkeypatch.setattr(checker, "load_direct_dependencies", lambda: [])
    monkeypatch.setattr(
        sys, "argv", ["x", "--strict", "--output", str(tmp_path / "report.md")]
    )
    assert checker.main() == 1


def test_deferral_matches_a_name_spelled_with_underscores(tmp_path: Path) -> None:
    """PyPI treats `typing_extensions` and `typing-extensions` as one project."""
    path = tmp_path / "deferrals.json"
    path.write_text(
        json.dumps(
            {
                "deferrals": {
                    "Typing-Extensions": {"deferredLatest": "5.0", "reason": "later"}
                }
            }
        ),
        encoding="utf-8",
    )
    deferrals = checker.load_deferrals(path)
    package = {
        "name": "typing_extensions",
        "minimum": "4.0",
        "requirement": "typing_extensions>=4.0",
        "source": "requirements-dev.txt",
        "hold": "",
    }
    original = checker.fetch_pypi_version
    checker.fetch_pypi_version = lambda name, timeout=10.0: "5.0"  # type: ignore
    try:
        (row,) = checker.collect_status([package], deferrals)
    finally:
        checker.fetch_pypi_version = original
    assert row["deferred_reason"] == "later"
    assert not checker.needs_review(row)


@pytest.mark.parametrize("payload", ["[]", '{"deferrals": []}', '{"deferrals": ["x"]}'])
def test_malformed_deferrals_file_is_ignored(tmp_path: Path, payload: str) -> None:
    path = tmp_path / "deferrals.json"
    path.write_text(payload, encoding="utf-8")
    assert checker.load_deferrals(path) == {}


@pytest.mark.parametrize("body", [b"[]", b'"x"', b"null"])
def test_unexpected_pypi_payload_shape_reads_as_check_failed(
    monkeypatch: pytest.MonkeyPatch, body: bytes
) -> None:
    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self):
            return body

    monkeypatch.setattr(
        checker.urllib.request, "urlopen", lambda *a, **k: Response()
    )
    assert checker.fetch_pypi_version("ruff") is None


def test_truncated_pypi_response_reads_as_check_failed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import http.client

    def boom(*args, **kwargs):
        raise http.client.IncompleteRead(b"{")

    monkeypatch.setattr(checker.urllib.request, "urlopen", boom)
    assert checker.fetch_pypi_version("ruff") is None
