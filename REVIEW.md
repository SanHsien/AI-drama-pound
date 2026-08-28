# Repository review（Windows-first）

- Review date: 2026-08-28
- Review baseline: `258be68885eb3e93291ca2273962cf27a565957b`（overlay 首推）；本輪關閉可修 finding 後見「修正後」
- Upstream reviewed through: `d3724f77466e93ee71778a73498b183eb1dca7bb`
- Upstream watermarks: PR / issue `reviewed_pr_through` / `reviewed_issue_through` = **0**
- Primary environment: Windows 11、PowerShell、Python 3.14（本機）、CI Ubuntu 3.9–3.14、Windows 3.14
- Status: 維護骨架可用；產品 `skill-src/` 未改寫；fork 可修的 R-01 已修；不回貢

## 結論

這個 fork 適合作為 Windows 本機安裝、並追蹤上游 AI 短劇編劇 skill 的維護線。產品是一個繁體中文 Markdown skill（`skill-src/ai-short-drama-screenwriter/`）；沒有獨立編劇引擎、沒有後端、沒有 Node CLI。

overlay 首推（`258be68`）之後，本輪做完整風險快照。**沒有**改寫產品 `SKILL.md`、**沒有**改 `validation/` 或 `docs/superpowers/`、**沒有**回貢。

## 本輪實證

### 審查當下（`258be68`）

```text
git rev-parse HEAD
→ 258be68885eb3e93291ca2273962cf27a565957b

gh repo set-default --view
→ SanHsien/AI-drama-pound

gh api repos/SanHsien/AI-drama-pound
→ fork=true, parent=POUND0423/AI-drama-pound, license=MIT

python tools/check_upstream_updates.py --strict
→ No new upstream commits. Nothing to review.

git ls-files -s CLAUDE.md
→ 100644（不是 120000）

git ls-files | 無 .env / credentials / cookies
git check-ignore cookies.txt credentials.json
→ 當時未被忽略（R-01）
```

GitHub Actions（SanHsien/AI-drama-pound，`258be68`）：

| Workflow | 結果 | 說明 |
|---|---|---|
| [CI](https://github.com/SanHsien/AI-drama-pound/actions/runs/33142618064) | success | Ubuntu py3.9–3.14 與 Windows `test (windows / py3.14)` 全綠 |
| [CodeQL](https://github.com/SanHsien/AI-drama-pound/actions/runs/33142617925) | success | Python `security-extended`；open alerts = 0 |
| [Upstream check](https://github.com/SanHsien/AI-drama-pound/actions/runs/33142617950) | success | |
| [Dependency freshness](https://github.com/SanHsien/AI-drama-pound/actions/runs/33142617911) | success | |

**沒有**用真實模型 API 跑上游 `validation/` 情境，**沒有**在 Codex / Claude Code / Cursor 實際安裝並觸發完整編劇流程，**沒有**對上游開 PR。

### 修正後

```text
pwsh -NoProfile -File tools\dev_check.ps1
→ compileall / ruff E9+F / pytest / validate_skills / check_links 全綠
→ 34 passed
→ 1 skill 通過；warnings 0
→ 16 份維護文件，0 斷連結
→ git check-ignore cookies.txt credentials.json drafts/episode.md → ignored
```

## 已修 findings

| ID | 嚴重度 | Finding | 修復 |
|---|---|---|---|
| R-01 | P3 | `.gitignore` 擋 `.env`，但不擋 `cookies.txt`／`credentials.json`，也沒有本機劇本草稿出口。`git check-ignore cookies.txt` 在 `258be68` 回未忽略。AGENTS.md 禁止提交劇本與憑證，但 git 不會擋。 | 加入 `cookies.txt`、`cookies.json`、`credentials.json`、`/drafts/`、`*.fountain`。`test_gitignore_covers_secrets_and_reports` 與 `test_gitignore_actually_ignores_user_secrets_and_drafts` 鎖行為。 |

## 已檢查、不列為 finding

- 產品現況：1 個 `skill-src/ai-short-drama-screenwriter/`，含 `SKILL.md`、`agents/openai.yaml`、`references/{workflow,format,checklists}.md`。frontmatter `name` 等於目錄名；`description` 含 `Use when`；SKILL.md 約 35 行（低於 500）。產品檔沒有 Claude Code `` !`command` ``。
- Fork overlay Python（`tools/check_*.py`、`tools/validate_skills.py`）無 `os.system`、`shell=True`、`eval(`、`exec(`、`pickle`。`check_upstream_updates.py` 以 argv 列表呼叫 `git`。`check_dependency_freshness.py` 只對 `pypi.org` 發 HTTPS（`# noqa: S310`）。
- `LICENSE` 維持上游 `Copyright (c) 2026 POUND0423` 原文；fork overlay 的 attribution 在 [`NOTICE.md`](NOTICE.md)，不把 LICENSE 改掛成第二作者原創。
- 公開入口只留繁中／英文；README 保留來源與 MIT credit，不轉載作者宣傳或社群。
- CI／CodeQL／upstream-check／dependency-freshness 的 checkout 已 pin SHA，且 `persist-credentials: false`。
- `gh repo set-default --view` 為 `SanHsien/AI-drama-pound`。不對上游開 PR、不 push `upstream`。
- Dependabot 不自動合併，合理。
- `CLAUDE.md` 從一開始就是一般檔，不是 git symlink。`git ls-files -s` 無 `120000`。
- 上游當時 0 個 open PR、0 個 open issue、只有 `main`；`check_upstream_updates.py --strict` 無新 commit。
- `pyproject.toml` 沒有 `[project]`／`[build-system]`。`.gitattributes` 釘 `eol=lf`。
- CodeQL open alerts = 0。`dev_check.ps1` **不含** Bandit；本線產品不是 Python 管線，不另加 Bandit 依賴。

## 尚未宣稱範圍

- **沒有**用真實模型 API 跑上游 `validation/` 情境，因此不宣稱八階段編劇流程已在本機壓過一輪。
- **沒有**在 Codex / Claude Code / Cursor 實際安裝並觸發完整編劇流程。
- **不宣稱** fork 有自己的 GitHub Release 或獨立產品版號；產品版本仍以上游 [v0.1.0](https://github.com/POUND0423/AI-drama-pound/releases/tag/v0.1.0) 為準。
- **不宣稱** 已把 overlay 送回上游。

## 建議下一步

1. 之後維護直接推 `origin/main`。回貢需當次對話明確同意。
2. 週排程 Upstream check 若再紅，先看是不是又有新 commit，不要把 watermark 往回退。
3. 上游若把作者社群或宣傳寫進 README，merge 後不要合進公開入口。
