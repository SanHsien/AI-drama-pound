from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import validate_skills  # noqa: E402


def test_audit_flags_missing_skill_file(tmp_path: Path) -> None:
    skill_dir = tmp_path / "ai-short-drama-screenwriter"
    skill_dir.mkdir()
    errors, _warnings = validate_skills.audit_skill(skill_dir)
    assert errors
    assert "Missing SKILL.md" in errors[0]


def test_audit_flags_name_mismatch(tmp_path: Path) -> None:
    skill_dir = tmp_path / "ai-short-drama-screenwriter"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(
        "---\nname: other-skill\ndescription: Use when writing ads.\n---\n\n# Ads\n",
        encoding="utf-8",
    )
    errors, _warnings = validate_skills.audit_skill(skill_dir)
    assert any("Name mismatch" in item for item in errors)


def test_audit_accepts_quoted_description(tmp_path: Path) -> None:
    skill_dir = tmp_path / "ai-short-drama-screenwriter"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(
        '---\nname: ai-short-drama-screenwriter\ndescription: "Use when writing a short drama."\n---\n\n# Skill\n',
        encoding="utf-8",
    )
    errors, warnings = validate_skills.audit_skill(skill_dir)
    assert errors == []
    assert warnings == []


def _skill(tmp_path: Path, body: str, encoding: str = "utf-8") -> Path:
    skill_dir = tmp_path / "demo-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_bytes(body.encode(encoding))
    return skill_dir


def test_audit_accepts_utf8_bom(tmp_path: Path) -> None:
    """Windows editors save a BOM; it is not a missing frontmatter."""
    skill_dir = _skill(
        tmp_path,
        "---\nname: demo-skill\ndescription: Use when demoing.\n---\n\n# Demo\n",
        "utf-8-sig",
    )
    errors, _warnings = validate_skills.audit_skill(skill_dir)
    assert errors == []


def test_audit_accepts_triple_dash_inside_a_value(tmp_path: Path) -> None:
    """A '---' inside the description must not cut the frontmatter short."""
    skill_dir = _skill(
        tmp_path,
        "---\nname: demo-skill\ndescription: Use when a --- rule is needed.\n---\n\n# Demo\n",
    )
    errors, _warnings = validate_skills.audit_skill(skill_dir)
    assert errors == []
    frontmatter = validate_skills.extract_frontmatter(
        (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    )
    assert (
        validate_skills.field_value(frontmatter, "description")
        == "Use when a --- rule is needed."
    )


def test_audit_reads_folded_description(tmp_path: Path) -> None:
    """`description: >` is the text on the following lines, not the character '>'."""
    skill_dir = _skill(
        tmp_path,
        "---\nname: demo-skill\ndescription: >\n  Use when demoing\n  a folded block.\n---\n\n# Demo\n",
    )
    assert (
        validate_skills.field_value(
            validate_skills.extract_frontmatter(
                (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            ),
            "description",
        )
        == "Use when demoing a folded block."
    )
    errors, warnings = validate_skills.audit_skill(skill_dir)
    assert errors == []
    assert warnings == []


def test_audit_flags_empty_description_instead_of_reading_next_line(
    tmp_path: Path,
) -> None:
    """`description:` with nothing after it must not swallow the next key."""
    skill_dir = _skill(
        tmp_path, "---\ndescription:\nname: demo-skill\n---\n\n# Demo\n"
    )
    errors, _warnings = validate_skills.audit_skill(skill_dir)
    assert "Missing 'description' field in frontmatter" in errors


def test_folded_description_with_trailing_comment_reads_the_block() -> None:
    """`description: > # note` is a folded scalar plus a YAML comment."""
    fm = "description: > # note\n  Use when x\n  happens.\nname: demo-skill\n"
    assert validate_skills.field_value(fm, "description") == "Use when x happens."


def test_plain_value_drops_trailing_yaml_comment() -> None:
    assert validate_skills.field_value("name: demo-skill  # dir name\n", "name") == (
        "demo-skill"
    )
