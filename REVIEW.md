# Repository review（Windows-first）

- Review date: 2026-08-28
- Review baseline: overlay 首推；產品 `skill-src/` 未改寫
- Upstream reviewed through: `d3724f77466e93ee71778a73498b183eb1dca7bb`
- Upstream watermarks: PR / issue `reviewed_pr_through` / `reviewed_issue_through` = **0**
- Primary environment: Windows 11、PowerShell、Python 3.14（本機）、CI Ubuntu 3.9–3.14、Windows 3.14
- Status: 維護骨架已落地；產品 skill 未改寫；本機 Windows gate 全綠；GitHub Actions 以 overlay 首推後的 run 為準

## 結論

這個 fork 適合作為 Windows 本機安裝、並追蹤上游 AI 短劇編劇 skill 的維護線。產品是一個繁體中文 Markdown skill（`skill-src/ai-short-drama-screenwriter/`）；沒有獨立編劇引擎、沒有後端、沒有 Node CLI。

本輪只加 Windows-first overlay。**沒有**改寫產品 `SKILL.md`、**沒有**改 `validation/` 或 `docs/superpowers/`、**沒有**回貢。

## 已檢查、不列為 finding

- 產品現況：1 個 `skill-src/ai-short-drama-screenwriter/`，含 `SKILL.md`、`agents/openai.yaml`、`references/{workflow,format,checklists}.md`。
- Fork overlay Python（`tools/check_*.py`、`tools/validate_skills.py`）無 `os.system`、`shell=True`、`eval(`、`exec(`、`pickle`。`check_upstream_updates.py` 以 argv 列表呼叫 `git`。
- 倉庫沒有提交 `.env`。
- 公開入口只留繁中／英文；README 保留來源與 MIT credit，不轉載作者宣傳。
- CodeQL / CI checkout 已 pin SHA，且 `persist-credentials: false`。
- `gh repo set-default --view` 為 `SanHsien/AI-drama-pound`。不對上游開 PR、不 push `upstream`。
- Dependabot 不自動合併，合理。
- `CLAUDE.md` 從一開始就是一般檔，不是 git symlink。

## 本輪實證

### 本機

```text
pwsh -NoProfile -File tools\dev_check.ps1
→ compileall / ruff E9+F / pytest / validate_skills / check_links 全綠
→ 33 passed
→ 1 skill 通過；warnings 0
→ 16 份維護文件，0 斷連結
```

## 尚未宣稱範圍

- **沒有**用真實模型 API 跑上游 `validation/` 情境。
- **沒有**在 Codex / Claude Code / Cursor 實際安裝並觸發完整編劇流程。
- `dev_check.ps1` **不含** Bandit；CodeQL 是獨立 workflow。
- GitHub Actions 結果以 overlay 首推後的 run 為準，本檔不預填尚未發生的 CI URL。
