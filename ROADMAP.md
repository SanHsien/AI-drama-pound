# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-10-29 依 `main` `76d6ff65e57c` 查的快照，開工前先重查 GitHub。

## 現況

這是 POUND0423/AI-drama-pound（繁體中文 AI 短劇編劇 Markdown skill）的 Windows-first 維護 fork，產品 `skill-src/` 未改寫。維護面健康：`main` 上 CI、CodeQL、Dependency freshness、Upstream check 最近一次皆 success，open PR 0 筆、Dependabot 與 Code scanning 告警 0 筆（2026-10-29 `gh` 查詢）；issue 功能在本 fork 已停用，故 issue 數「未查到」，不是 0。上游水位 `reviewed_through` 為 `d3724f77466e`，上游最後 push 2026-08-26，無待審項目（`tools/upstream_baseline.json`）。

## 近期：可以直接動手

| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 無 | 維護骨架已完整，沒有未處理的告警、PR、上游項目；為了讓清單好看而造工作會違反 `AGENTS.md` 精神 | 開工前重跑 `gh api repos/SanHsien/AI-drama-pound/dependabot/alerts?state=open` 與 `python tools/check_upstream_updates.py --strict`，結果為空才維持「無」 | 維護者 | 2026-10-29 `gh` 查詢；`tools/upstream_baseline.json` |

## 中期：等條件成立再做

| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 引進上游新 commit／PR／issue | `Upstream check` workflow 轉 failure（＝上游有未審項目） | 逐項審完，`tools/upstream_baseline.json` 水位推進；`python tools/check_upstream_updates.py --strict` exit 0；`tools\dev_check.ps1` 綠 | Claude Sonnet | `tools/upstream_baseline.json`；`docs/UPSTREAM.md` |
| 用真實模型實跑上游 `validation/` 情境，並在 Codex／Claude Code／Cursor 實際安裝觸發八階段流程 | 維護者決定要對外宣稱編劇流程可用，且願意負擔模型 API 費用與 GUI 實機操作 | 每個情境留下輸入、輸出與通過／失敗紀錄，寫入 `REVIEW.md`「尚未宣稱範圍」並更新該段；未實跑的環境維持不宣稱 | 維護者 | `REVIEW.md:98-101` |
| 取消 pytest 的 `freshness-hold`、升到 pytest 9 | CI 矩陣放棄 Python 3.9（pytest 9 需 Python >=3.10） | `.github/workflows/ci.yml` 矩陣不含 3.9、`requirements-dev.txt` 移除該 hold、CI 全綠、`check_dependency_freshness.py --strict` exit 0 | Codex | `requirements-dev.txt:2`；`.github/workflows/ci.yml:25` |

## 刻意不做

| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 改寫產品 `skill-src/`、`validation/`、`docs/superpowers/` | 以上游為準，除非有已記錄的 fork 修正（`FORK.md`、`REVIEW.md` 結論） | 上游停止維護且維護者決定接手產品開發 |
| 對上游開 PR／回貢 | 維護者決定不回貢（`REVIEW.md:5`） | 維護者在新的對話中明確要求回貢 |
| 啟用 Dependabot 自動合併 | 決策：合併前仍要人工讀 diff（`docs/DECISIONS.md:29-33`） | 依賴增加到人工讀 diff 成為瓶頸 |
| 把 `check_links.py` 擴到上游產品目錄 | 上游連結會因每次同步而變，打斷本線 CI（`REVIEW.md` R-06） | 產品 SKILL.md 開始含相對連結且上游承諾穩定 |

## 維護方式

fork：以 `Upstream check` workflow 為訊號，failure 時審上游項目並推進水位，採用與否的理由記在 `docs/DECISIONS.md`。直接推 `main`（`docs/DECISIONS.md:17-27`）；Dependabot 只開 PR，人工讀 diff 後合併。
