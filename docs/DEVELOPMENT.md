# 開發環境

維護者與 AI 接手用的開發文件。產品使用方式在 [`README.md`](../README.md)；上游同步在 [`UPSTREAM.md`](UPSTREAM.md)；決策在 [`DECISIONS.md`](DECISIONS.md)。

## 架構

```text
skill-src/ai-short-drama-screenwriter/
        ├── SKILL.md           產品 skill（繁體中文，以上游為準）
        ├── agents/openai.yaml Codex 顯示與隱式啟動設定
        └── references/        流程、格式、修改清單（按需載入）
        │
        ▼
 安裝到 ~/.agents/skills、~/.claude/skills 或 ~/.cursor/skills 後才真正可被呼叫

validation/                    上游定性驗收紀錄，不是 pytest
docs/superpowers/              上游設計與實作計畫
```

`skill-src/`、`validation/`、`docs/superpowers/` 是要安裝或跟隨上游的產品。其餘檔案是本 fork 的開發與治理骨架，不要一起複製進 skills 目錄。

## 本機開發（Windows）

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
$env:PYTHONUTF8 = "1"
pwsh -NoProfile -File tools\dev_check.ps1
```

先決條件：Python 3.14（CI 另測 3.9–3.14）、PowerShell 7。

只驗證產品入口是否齊全時，確認：

- `skill-src/ai-short-drama-screenwriter/SKILL.md`
- `skill-src/ai-short-drama-screenwriter/agents/openai.yaml`
- `skill-src/ai-short-drama-screenwriter/references/workflow.md`
- `skill-src/ai-short-drama-screenwriter/references/format.md`
- `skill-src/ai-short-drama-screenwriter/references/checklists.md`

gate 驗的是規格、語法與維護腳本，不會呼叫模型去寫劇本。

## Canonical gate

`tools\dev_check.ps1` 會依序：

1. `python -m compileall`（`tests` 與 `tools` 底下的 `.py`）
2. `ruff check`（E9 + F）
3. `pytest tests/ -q`
4. `python tools/validate_skills.py`
5. `python tools/check_links.py`

CI 在 Ubuntu 跑 3.9–3.14，並加一個 Windows Python 3.14 job 跑同一套 gate。推 `main` 前先跑本機 gate。

## 工具設定

`pyproject.toml` **只放工具設定**，沒有 `[project]` 與 `[build-system]`：本 repo 交付的是 Markdown Agent Skill，不是 Python 套件。改 `ci.yml` 的 ruff 旗標時要同步改 `pyproject.toml`，`tests/test_docs.py::test_tool_config_matches_ci_flags` 會擋住漂移。`.python-version` 釘 3.14。

`.gitattributes` 把行尾釘成 LF。沒有它，全域 `core.autocrlf=true` 會讓工作區變 CRLF，於是 `git status` 顯示檔案 modified 但 `git diff` 是空的。

## 依賴新鮮度

`tools/check_dependency_freshness.py` 把 `requirements-dev.txt` 宣告的每一筆直接依賴拿去對 PyPI 現行版本，`.github/workflows/dependency-freshness.yml` 每月跑一次。紅燈只有兩條誠實出口：`# freshness-hold:`（常態政策）或 `.github/dependency-deferrals.json` 的 `deferredLatest`（會過期）。調高宣告下限來讓報告變綠不是出口。

## 不要做的事

- 不要把產品 `SKILL.md` 改寫成維護索引。
- 不要改寫 `validation/` 或 `docs/superpowers/` 來記錄 fork 文件。
- 不要提交 `.env`、使用者劇本或未公開故事材料。
- 測試必須是靜態規格檢查，不能打真實模型 API 來當 CI。
