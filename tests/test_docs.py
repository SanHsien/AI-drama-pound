from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import check_links  # noqa: E402
import validate_skills  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def test_every_skill_directory_has_valid_frontmatter() -> None:
    skill_dirs = validate_skills.iter_skill_dirs()
    assert [path.name for path in skill_dirs] == ["ai-short-drama-screenwriter"]
    failures = []
    for skill_dir in skill_dirs:
        errors, _warnings = validate_skills.audit_skill(skill_dir)
        if errors:
            failures.append(f"{skill_dir.name}: {errors}")
    assert failures == []


def test_product_skill_keeps_required_files() -> None:
    skill = ROOT / "skill-src" / "ai-short-drama-screenwriter"
    assert (skill / "SKILL.md").is_file()
    assert (skill / "agents" / "openai.yaml").is_file()
    for name in ("workflow.md", "format.md", "checklists.md"):
        assert (skill / "references" / name).is_file()


def test_maintainer_markdown_links_resolve() -> None:
    failures = 0
    for path in check_links.iter_documents():
        problems = check_links.check_document(path)
        failures += len(problems)
        for problem in problems:
            print(f"{path}: {problem}")
    assert failures == 0


def test_ci_covers_python_314() -> None:
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert '"3.14"' in workflow
    assert "windows / py3.14" in workflow


def test_issue_contact_links_point_at_this_fork() -> None:
    text = (ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text(
        encoding="utf-8"
    )
    assert "SanHsien/AI-drama-pound/blob/main/CONTRIBUTING.md" in text
    assert "POUND0423/AI-drama-pound" in text


def test_public_docs_are_traditional_chinese_and_english_only() -> None:
    for name in ("README.ja.md", "README.zh-CN.md", "README.zh.md"):
        assert not (ROOT / name).exists(), name
    for name in ("README.md", "README.en.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        assert "README.ja.md" not in text
        assert "README.zh-CN.md" not in text


def test_readme_keeps_credit_without_author_promotion() -> None:
    zh = (ROOT / "README.md").read_text(encoding="utf-8")
    en = (ROOT / "README.en.md").read_text(encoding="utf-8")
    for name, text in (("README.md", zh), ("README.en.md", en)):
        assert "POUND0423/AI-drama-pound" in text, name
        assert "NOTICE.md" in text, name
        assert "MIT" in text, name
        assert "SanHsien/AI-drama-pound" in text, name
    assert r"~\.agents\skills" in zh
    assert r"~\.cursor\skills" in zh
    assert "切黑" in zh
    assert "切黑" in en
    assert "阿澤" in en


def test_bilingual_pairs_cross_link_each_other() -> None:
    for zh_name, en_name in (("README.md", "README.en.md"), ("CHANGELOG.md", "CHANGELOG.en.md")):
        zh = ROOT / zh_name
        en = ROOT / en_name
        assert zh.is_file(), f"missing {zh_name}"
        assert en.is_file(), f"missing {en_name}"
        assert en_name in zh.read_text(encoding="utf-8"), f"{zh_name} does not link {en_name}"
        assert zh_name in en.read_text(encoding="utf-8"), f"{en_name} does not link {zh_name}"


def test_changelog_records_fork_history_not_upstream_product_history() -> None:
    text = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "docs/UPSTREAM.md" in text
    assert "docs/DECISIONS.md" in text
    assert "POUND0423/AI-drama-pound" in text


def test_tool_config_matches_ci_flags() -> None:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert 'target-version = "py39"' in pyproject
    assert "--target-version py39" in ci
    assert 'select = ["E9", "F"]' in pyproject
    assert "--select E9,F" in ci
    assert not re.search(r"^\[project\]", pyproject, re.M)
    assert not re.search(r"^\[build-system\]", pyproject, re.M)


def test_line_endings_are_pinned_to_lf() -> None:
    attrs = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "* text=auto eol=lf" in attrs
    for suffix in ("*.md", "*.py", "*.ps1"):
        assert suffix in attrs


def test_gitignore_covers_secrets_and_reports() -> None:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert ".env" in text
    assert ".venv/" in text
    assert "upstream-review-report.md" in text
    assert "cookies.txt" in text
    assert "credentials.json" in text
    assert "/drafts/" in text
    assert "*.fountain" in text
    assert "*.docx" in text


def test_gitignore_actually_ignores_user_secrets_and_drafts() -> None:
    for name in ("cookies.txt", "credentials.json", "drafts/episode.md", "scene.docx"):
        result = subprocess.run(
            ["git", "check-ignore", "-q", name],
            cwd=ROOT,
            check=False,
        )
        assert result.returncode == 0, name


def test_review_md_is_a_risk_snapshot() -> None:
    review = (ROOT / "REVIEW.md").read_text(encoding="utf-8")
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "Windows-first" in review
    assert "R-01" in review
    assert "R-02" in review
    assert "風險快照" in agents
    assert "`REVIEW.md`" in agents


def test_product_skill_has_no_claude_bang_commands() -> None:
    text = (
        ROOT / "skill-src" / "ai-short-drama-screenwriter" / "SKILL.md"
    ).read_text(encoding="utf-8")
    assert "!`" not in text


def test_tracked_files_are_not_git_symlinks() -> None:
    result = subprocess.run(
        ["git", "ls-files", "-s"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    symlinks = [
        line.split("\t", 1)[-1]
        for line in result.stdout.splitlines()
        if line.startswith("120000 ")
    ]
    assert symlinks == [], f"git symlink 會讓 Windows checkout 失敗: {symlinks}"


def test_check_links_rejects_path_outside_repo(tmp_path: Path) -> None:
    doc = tmp_path / "note.md"
    doc.write_text("[here](.)\n", encoding="utf-8")
    problems = check_links.check_document(doc)
    assert any("逃出" in item for item in problems)


@pytest.fixture
def link_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(check_links, "ROOT", tmp_path.resolve())
    (tmp_path / "target.md").write_text("# t\n", encoding="utf-8")
    return tmp_path.resolve()


@pytest.mark.parametrize(
    "link",
    [
        '[a](target.md "A title")',
        "[a](target.md 'A title')",
        "[a](target.md?plain=1)",
        "[a](<target.md>)",
    ],
)
def test_check_links_accepts_valid_link_syntax(link_root: Path, link: str) -> None:
    doc = link_root / "note.md"
    doc.write_text(link + "\n", encoding="utf-8")
    assert check_links.check_document(doc) == []


def test_check_links_ignores_fenced_code_examples(link_root: Path) -> None:
    doc = link_root / "note.md"
    doc.write_text(
        "```md\n[example](does-not-exist.md)\n```\n\n~~~\n[x](also-missing.md)\n~~~\n",
        encoding="utf-8",
    )
    assert check_links.check_document(doc) == []


def test_check_links_still_reports_a_missing_target_with_a_title(
    link_root: Path,
) -> None:
    doc = link_root / "note.md"
    doc.write_text('[a](missing.md "A title")\n', encoding="utf-8")
    problems = check_links.check_document(doc)
    assert len(problems) == 1 and "missing.md" in problems[0]


def test_check_links_indented_closing_fence_does_not_hide_later_links(
    link_root: Path,
) -> None:
    doc = link_root / "note.md"
    doc.write_text("```\na\n   ```\n[x](missing.md)\n", encoding="utf-8")
    assert len(check_links.check_document(doc)) == 1


def test_check_links_html_src_with_a_space_is_checked_whole(link_root: Path) -> None:
    (link_root / "my image.png").write_bytes(b"x")
    doc = link_root / "note.md"
    doc.write_text('<img src="my image.png">\n', encoding="utf-8")
    assert check_links.check_document(doc) == []


def test_quoted_gt_description_is_a_literal_not_a_block_scalar() -> None:
    assert validate_skills.field_value("description: '>'\n", "description") == ">"


def test_block_scalar_indicator_accepts_either_order() -> None:
    fm = "description: >2-\n  use when x\n"
    assert validate_skills.field_value(fm, "description") == "use when x"
