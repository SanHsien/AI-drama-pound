# 維護決策

## 2026-08-28：建立 Windows-first 維護型 fork

**決定**：fork `POUND0423/AI-drama-pound`，保留 MIT 與完整歷史，預設分支維持 `main` 以降低與上游同步摩擦。本線聚焦繁中／英文公開入口、Windows 開發 gate、Windows CI，以及逐筆審查的上游追蹤。

**理由**：上游已有可安裝的 `ai-short-drama-screenwriter` skill、定性驗證紀錄與 MIT 授權，符合維護者讓 AI 助手寫短劇劇本的需求。缺的是 Windows 11 上可重現的開發／驗收骨架，以及與其他 SanHsien fork 一致的治理文件。直接用上游 repo 難以長期記錄 fork 取捨。

**限制**：

- 不把 fork 包裝成原創專案，不移除原作者與 MIT 標示。
- `skill-src/*/SKILL.md` 保持產品規格，不用維護索引覆寫。
- 不把產品 skill 改寫成另一種中文；產品語言跟隨上游（已是繁體中文）。
- 上游更新必須逐筆審查。
- 不回貢，除非維護者在當次對話明確同意。

## 2026-08-28：維護線直接推 main

**決定**：fork 維護不再開功能分支。改完在本機跑 gate，通過後直接推 `origin/main`。遠端只留 `main`；`upstream/main` 只追蹤。

**理由**：這是單人維護 fork，分支與 PR 沒有第二審查者，只增加同步成本。

**限制**：

- Dependabot 與外部 fork 仍可能開 PR，讀 diff 後再合併，不自動合併。
- 不推 `upstream`，不 force-push `main`。
- 不刪 `upstream` remote。

## 2026-08-28：不啟用 Dependabot 自動合併

**決定**：Dependabot 只開 PR；CI 與人工讀 diff 通過後才合併。

**理由**：開發依賴只有 pytest / ruff，體積小，但自動合併仍會跳過「讀 diff」這一步。

## 2026-08-28：公開文件只留繁中與英文；README 只留 credit

**決定**：GitHub About 與公開入口只用繁體中文與英文。README 不轉載作者個人社群或宣傳。來源與授權 credit 留在 README 短段與 `NOTICE.md`。

**理由**：這是維護型 fork，不是原作者的宣傳頁。相關 credit 放 README 短段與 `NOTICE.md` 即可滿足 MIT 標示。

**限制**：上游若把宣傳段落一併推進來，merge 後刪掉／不要合進公開入口。產品說明與安裝步驟可同步。

## 2026-08-28：產品 skill 維持 skill-src/ 目錄契約

**決定**：本 fork 不把 `skill-src/ai-short-drama-screenwriter/` 搬到 repo 根目錄或改名。安裝說明仍是「複製該資料夾到宿主 skills 目錄」。

**理由**：上游 README、validation 路徑與 `agents/openai.yaml` 都綁這個目錄名。搬運會讓每次上游同步變成衝突。

**限制**：`tools/validate_skills.py` 掃 `skill-src/*/`，`name` 必須等於目錄名。

## 2026-08-28：CLAUDE.md 存一般檔，不做 git symlink

**決定**：本 fork 的 `CLAUDE.md` 以一般檔（mode `100644`）存放 fork 薄入口。

**理由**：其他 fork 的經驗是 git symlink 會讓 Windows CI checkout 失敗（`Filename too long`）。本線從一開始就存一般檔。

**限制**：同步上游時若出現 `CLAUDE.md` symlink，必須再改成一般檔。`tests/test_docs.py::test_tracked_files_are_not_git_symlinks` 會擋住。

## 2026-08-29：上游檢查補上 PR 與 issue 兩個面向

**決定**：`check_upstream_updates.py` 補上以 `--state all` 收集上游 PR／issue 的邏輯，
`upstream-check.yml` 補 `GH_TOKEN: ${{ github.token }}`，新增 `tests/test_upstream_updates.py`。
Baseline 既有的水位不動。

**理由**：`docs/UPSTREAM.md` 早就寫著「四個面向都要看」，`upstream_baseline.json` 也記著
`reviewed_pr_through` 與 `reviewed_issue_through`——但**沒有任何程式讀那兩個欄位**，檢查器只比對
commit 水位。那兩個面向不是「查過沒發現」，是根本沒查，而每週的排程報告長得跟查過一樣綠。
這是艦隊層級的問題：24 個 fork 裡 21 個都這樣（`SanHsien/repo-fleet-ops` 的 `docs/INCIDENTS.md`
第十條）。參考實作是 `SanHsien/harness-guard`。

三個性質，缺一不可：

- **`--state all`**：只查 `open` 看不到「開了又關、沒有合併」的 PR，而那正是「上游拒收、但可能對
  本 fork 有價值」的一類——已合併的遲早會經由 commit 抵達，被關掉的永遠不會。
- **`gh` 失敗時回 `None` 不回 `[]`**，報告寫 `Not checked` 並 **fail closed**（exit 2）。
  「沒查到」和「沒有」在綠色報告裡長得一樣，只有一個是真的。
- **`GH_TOKEN`**：`gh` 在 Actions 裡沒有憑證就列舉不到，配上 fail closed 會讓紅燈的意思變成
  「檢查器壞了」而不是「上游有東西」。

**證據**：落地後實跑 `python tools/check_upstream_updates.py`，三個面向都印出水位與待辦數；
本 repo 的 gate 全綠。

**已知代價**：水位以上真的有東西時，每週的 upstream-check 會回 exit 1。那是它該做的事——先前的
綠燈不是「沒有待辦」，是沒有人看。

**觸發條件**：報告列出項目時逐筆讀 diff、把採用／略過理由寫進本檔，然後才推進 baseline 的水位。
