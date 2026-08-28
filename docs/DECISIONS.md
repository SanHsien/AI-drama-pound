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
