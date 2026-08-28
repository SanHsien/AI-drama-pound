English | [中文版](CHANGELOG.md)

# Changelog

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); newest first.
This file records **this fork's maintenance history** only (from 2026-08-28). The product
history of upstream
[`POUND0423/AI-drama-pound`](https://github.com/POUND0423/AI-drama-pound) lives in
its own history and in the review ledger at [`docs/UPSTREAM.md`](docs/UPSTREAM.md). Per-commit
adopt/skip reasoning is recorded in [`docs/DECISIONS.md`](docs/DECISIONS.md).

---

## 2026-08-28

### Added

- **Windows-first maintenance overlay.** `AGENTS.md`, `CLAUDE.md`, `FORK.md`, `NOTICE.md`,
  `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `docs/`, maintenance scripts under
  `tools/`, `tests/`, and GitHub workflows for CI, CodeQL, Dependabot, upstream review, and
  dependency freshness. CI runs Ubuntu 3.9–3.14 plus Windows Python 3.14: pytest, ruff (E9+F),
  `validate_skills.py`, and relative-link checks.
- **Public entry in Traditional Chinese and English only.** `README.md` stays the Chinese
  primary file; `README.en.md` is the English mirror. Source and license credit stay;
  author promotion does not.
