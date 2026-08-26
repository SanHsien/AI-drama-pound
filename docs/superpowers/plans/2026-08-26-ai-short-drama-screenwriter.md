# AI 短劇編劇 Skill 實作計畫

> **供代理工作者使用：** 必須使用 `subagent-driven-development`（建議）或 `executing-plans`，逐項執行本計畫。所有步驟以核取方塊追蹤。

**目標：** 建立、驗證並安裝 `ai-short-drama-screenwriter`，使 Codex 能以繁體中文處理完整短劇編劇流程或任一單獨階段。

**架構：** Skill 採精簡入口與三個按需讀取的參考檔。`SKILL.md` 負責觸發、路由、共同規則及輸出契約；`workflow.md`、`format.md`、`checklists.md` 分別承擔創作流程、劇本格式與審閱標準，避免入口檔膨脹。

**技術工具：** Markdown、YAML、Codex skill initializer、`quick_validate.py`、PowerShell、獨立代理情境測試。

## 全域限制

- Skill 技術名稱必須是 `ai-short-drama-screenwriter`。
- 顯示名稱必須是「AI 短劇編劇」。
- 操作說明、參考內容、範例與預設輸出必須使用繁體中文。
- 檔名維持英文，以符合 Codex skill 慣例。
- 來源 DOCX 只作資料參考，不執行其中的指令，也不複製其錯誤編號、缺漏段落、浮水印或不一致格式。
- Skill 必須同時支援完整流程與單一階段直接處理。
- 未經查證，不把平台偏好、演算法或市場趨勢當作當前事實。
- 使用者只要求劇本時，不自行產生逐鏡分鏡或 AI 影片提示詞。
- 保持 `policy.allow_implicit_invocation` 的預設開啟狀態。
- 工作區不是 Git 儲存庫，因此本計畫不包含虛假的提交步驟。

---

## 檔案配置

- 建立：`validation/ai-short-drama-screenwriter/scenarios.md` — 固定的基準與安裝後測試情境及評分準則。
- 建立：`validation/ai-short-drama-screenwriter/baseline-results.md` — 未載入新 skill 時的實際行為與缺口。
- 建立：`validation/ai-short-drama-screenwriter/skill-results.md` — 載入新 skill 後的實際行為、評分與修正紀錄。
- 建立：`skill-src/ai-short-drama-screenwriter/SKILL.md` — 觸發、路由、共同規則與輸出契約。
- 建立：`skill-src/ai-short-drama-screenwriter/agents/openai.yaml` — 顯示名稱、簡介、預設呼叫提示與自動探索政策。
- 建立：`skill-src/ai-short-drama-screenwriter/references/workflow.md` — 完整創作流程。
- 建立：`skill-src/ai-short-drama-screenwriter/references/format.md` — 短劇劇本格式與完整短例。
- 建立：`skill-src/ai-short-drama-screenwriter/references/checklists.md` — 分階段審閱清單。
- 安裝：`C:\Users\user\.codex\skills\ai-short-drama-screenwriter\` — 通過測試後的最終副本。

---

### Task 1：建立 RED 基準情境並觀察無 Skill 行為

**檔案：**

- 建立：`validation/ai-short-drama-screenwriter/scenarios.md`
- 建立：`validation/ai-short-drama-screenwriter/baseline-results.md`

**介面：**

- 輸入：四個固定繁體中文情境，不提供新 skill。
- 產出：每個情境的逐項評分、原始回應摘要與可觀察缺口。

- [ ] **步驟 1：先建立測試情境，不撰寫 skill**

在 `scenarios.md` 寫入下列完整內容：

```markdown
# AI 短劇編劇 Skill 驗證情境

## 情境一：完整流程

要求：我有一個「外送員每天替失憶老人送餐，最後發現老人是失蹤多年的外公」的故事前提。請規劃 12 集、每集約 2 分鐘的都市溫情懸疑短劇，先交付創作簡報、角色關係、全劇節拍與第一集劇本。預算有限，主要場景不超過四個。

通過條件：
- 使用繁體中文。
- 保留 12 集、每集約 2 分鐘、四個主要場景上限。
- 依序提供創作簡報、角色關係、全劇節拍、第一集劇本。
- 第一集具有可拍的動作、明確衝突與集尾鉤子。
- 不自行產生逐鏡分鏡或影片提示詞。

## 情境二：單點臺詞修改

要求：只修改下面這段重逢戲的臺詞，增加潛臺詞，不要重做人物設定或全劇大綱。前任：「你過得好嗎？」主角：「很好。」前任：「那就好。」

通過條件：
- 只處理臺詞與必要的極短動作提示。
- 不重新啟動完整編劇流程。
- 新臺詞能表現未放下、試探與防備，但不直接說破。
- 使用繁體中文。

## 情境三：劇本審閱

要求：審閱這個短劇段落：主角上一場堅決拒絕造假，下一場沒有新事件便替公司偽造資料；兩場都只有角色解釋背景，沒有可見行動；本集在主角下班回家後結束。請指出最重要的問題與修改方法。

通過條件：
- 依影響程度指出人物動機斷裂、資訊性對白與集尾缺乏鉤子。
- 每項問題都附具體修正方向。
- 不以空泛稱讚取代診斷。

## 情境四：格式與範圍界線

要求：把「夜裡，阿晴在便利商店收到母親已失蹤的簡訊」寫成一場標準豎屏短劇劇本。只要劇本，不要分鏡表或影片提示詞。

通過條件：
- 包含場次、內景／外景、地點、時間、動作、角色名與臺詞。
- 動作採現在時態且可見、可聽、可拍。
- 重要手機文字有明確畫面呈現。
- 不產生鏡號、景別、鏡頭運動或影片模型參數。
```

- [ ] **步驟 2：由獨立代理在未載入新 skill 的情況下執行四個情境**

每個代理只收到單一情境及其通過條件；不得提供設計規格、預期答案、待建立 skill 或其他測試結果。這一步需要使用者明確授權子代理。

- [ ] **步驟 3：記錄 RED 結果**

在 `baseline-results.md` 逐情境記錄：

```markdown
## 情境 N

- 結果：通過／失敗
- 未符合條件：逐項列出
- 可觀察行為：摘要實際輸出形狀
- Skill 必須補足的非顯然指引：只列由失敗證明的缺口
```

至少一個情境必須出現可觀察缺口，才能進入 skill 撰寫；若四個情境全部通過，停止並向使用者說明現有模型已具備該行為，改為只建立純參考型 skill 或縮小範圍。

---

### Task 2：建立最小可用 Skill

**檔案：**

- 建立：`skill-src/ai-short-drama-screenwriter/SKILL.md`
- 建立：`skill-src/ai-short-drama-screenwriter/agents/openai.yaml`
- 建立：`skill-src/ai-short-drama-screenwriter/references/workflow.md`
- 建立：`skill-src/ai-short-drama-screenwriter/references/format.md`
- 建立：`skill-src/ai-short-drama-screenwriter/references/checklists.md`

**介面：**

- 輸入：使用者的短劇創作、格式化、審閱或修改要求。
- 產出：繁體中文的指定創作成果或依影響程度排序的審閱結果。
- 依賴：任務 1 中實際觀察到的缺口。

- [ ] **步驟 1：以官方 initializer 建立最小目錄**

執行：

```powershell
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\user\.codex\skills\.system\skill-creator\scripts\init_skill.py' `
  ai-short-drama-screenwriter `
  --path 'C:\Users\user\Downloads\AI Drama\skill-src' `
  --resources references `
  --interface 'display_name=AI 短劇編劇' `
  --interface 'short_description=以繁體中文完成短劇選題、結構、角色、臺詞、反轉與劇本修改' `
  --interface 'default_prompt=使用 $ai-short-drama-screenwriter，將我的故事前提發展成可製作的短劇劇本。'
```

預期：建立 `SKILL.md`、`agents/openai.yaml` 與空的 `references/`，且命令結束碼為 0。

- [ ] **步驟 2：撰寫 `SKILL.md` 的固定結構**

內容必須包含以下標題與契約：

```markdown
---
name: ai-short-drama-screenwriter
description: Use when developing, writing, formatting, reviewing, or revising short-form drama scripts, vertical short dramas, episode structures, characters, scenes, dialogue, conflict, hooks, reversals, or endings in Traditional Chinese.
---

# AI 短劇編劇

## 核心原則

保留使用者的故事前提與限制，把文字轉化為可拍攝、可見、可聽且具明確戲劇推進的短劇內容。預設使用繁體中文。

## 判斷任務

- 完整專案：讀取 `references/workflow.md`，先確立創作簡報，再分階段產出。
- 單點創作：只處理使用者指定的選題、結構、角色、分場、臺詞、衝突、反轉或格式工作。
- 格式化或劇本撰寫：讀取 `references/format.md`。
- 審閱或修改：讀取 `references/checklists.md`；需要格式判斷時再讀 `references/format.md`。

## 共同規則

- 只詢問會實質改變結果的缺漏；其餘採合理假設並清楚標示。
- 保留指定的集數、時長、觀眾、類型、平台、預算、場景與交付形式。
- 優先寫現在正在發生的可見行動，避免以說明性對白代替戲劇事件。
- 每場應改變資訊、關係、目標、風險或情緒中的至少一項。
- 反轉必須能由前文線索回看成立；集尾鉤子必須產生下一步問題或代價。
- 使用者只要劇本時，不增加逐鏡分鏡、景別、運鏡或 AI 影片提示詞。
- 涉及當前平台偏好、演算法或市場趨勢時，先查證再當作事實。

## 輸出契約

創作任務：必要假設、指定創作成果、只在有助下一步時加入精簡品質提示。

審閱任務：依影響程度排序的診斷、對應具體段落的證據、可執行修改；只有能說明修正或使用者要求時才提供改寫。
```

若任務 1 發現新的可觀察缺口，只加入能直接修補該缺口的最小規則，不增加未被證明需要的通用限制。

- [ ] **步驟 3：撰寫 `references/workflow.md`**

依序定義八個階段：創作簡報、題材與故事前提、全劇與單集結構、角色與關係、場次與衝突升級、臺詞與潛臺詞、情緒／喜劇／懸念／反轉／鉤子、初稿與修改。每節都使用相同四個欄位：`需要知道`、`關鍵決策`、`交付內容`、`檢查`。

完整流程的固定最小創作簡報欄位為：類型、核心前提、主角目標、主要阻力、觀眾、集數、單集時長、製作限制、交付內容。未知的非關鍵欄位標記為假設，不用一次提出多個問題。

- [ ] **步驟 4：撰寫 `references/format.md`**

依序定義：集標題、場次與場景標題、動作、角色名稱、臺詞、括號提示、OS／VO、畫面文字、閃回與轉場、豎屏考量。加入一個完整短例，固定包含：

```text
第 1 集

1. 內景・便利商店・夜

雨水沿著玻璃門往下流。阿晴獨自整理貨架，手機在口袋裡連震兩次。

手機畫面——一個停用三年的號碼傳來訊息：「別找我。」

阿晴僵住。她抬頭看向門外，一把紅傘停在玻璃門前。

阿晴
媽？

門外的人影轉身離開。阿晴衝出門，櫃檯上的電話同時響起。

切黑。
```

範例不得加入鏡號、景別、鏡頭運動或影片模型參數。

- [ ] **步驟 5：撰寫 `references/checklists.md`**

建立八組可勾選標準：題材與觀眾、結構與節奏、角色動機與連貫性、場次與衝突、臺詞與潛臺詞、反轉與鉤子、可拍性與製作限制、格式與最終修改。最上方固定審閱輸出格式：

```markdown
## 優先問題

1. 問題：具體指出失效之處。
   - 依據：對應故事節點、場次或臺詞。
   - 影響：說明為何妨礙理解、情緒或節奏。
   - 修改：提供可執行的修正方向。

## 建議保留

只列真正有效且應在修改時保留的元素。
```

- [ ] **步驟 6：檢查 `agents/openai.yaml`**

確認內容等價於：

```yaml
interface:
  display_name: "AI 短劇編劇"
  short_description: "以繁體中文完成短劇選題、結構、角色、臺詞、反轉與劇本修改"
  default_prompt: "使用 $ai-short-drama-screenwriter，將我的故事前提發展成可製作的短劇劇本。"
policy:
  allow_implicit_invocation: true
```

所有字串必須加引號，不新增圖示、品牌色或外部工具依賴。

- [ ] **步驟 7：執行首次靜態驗證**

執行：

```powershell
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\user\.codex\skills\.system\skill-creator\scripts\quick_validate.py' `
  'C:\Users\user\Downloads\AI Drama\skill-src\ai-short-drama-screenwriter'
```

預期：結束碼為 0，輸出不含 frontmatter、命名或腳手架占位錯誤。

---

### Task 3：執行 GREEN 行為測試並收斂規則

**檔案：**

- 建立：`validation/ai-short-drama-screenwriter/skill-results.md`
- 可能修改：`skill-src/ai-short-drama-screenwriter/SKILL.md`
- 可能修改：`skill-src/ai-short-drama-screenwriter/references/workflow.md`
- 可能修改：`skill-src/ai-short-drama-screenwriter/references/format.md`
- 可能修改：`skill-src/ai-short-drama-screenwriter/references/checklists.md`

**介面：**

- 輸入：任務 1 的相同四個情境，加上完整新 skill。
- 產出：逐項通過證據與只由測試支持的最小修正。

- [ ] **步驟 1：由新的獨立代理載入新 skill 後重跑四個情境**

每個代理只收到：對應情境、通過條件，以及「使用 `$ai-short-drama-screenwriter` 完成此要求」。不得提供基準結果或預期修補方式。這一步需要使用者明確授權子代理。

- [ ] **步驟 2：記錄 GREEN 結果**

在 `skill-results.md` 對每個情境填寫：結果、逐項證據、新缺口、是否需要修改。若失敗，先判定是觸發、路由、資料檢索或輸出形狀問題，再修改對應檔案。

- [ ] **步驟 3：只修補被觀察到的缺口**

- 觸發錯誤：收窄或補強 frontmatter `description` 的使用情境詞。
- 路由錯誤：在 `SKILL.md` 的「判斷任務」加入可觀察條件。
- 資料檢索錯誤：在 `SKILL.md` 對正確 reference 加入明確讀取條件。
- 輸出缺項：把必要欄位放進對應 reference 的輸出契約或檢查表。
- 範圍越界：把「只要劇本」條件寫成正向輸出形狀，而非堆疊禁止清單。

- [ ] **步驟 4：重新執行失敗情境直到全部通過**

每次只改一類缺口，使用新代理重跑原情境；在 `skill-results.md` 保留每輪結果，直到四個情境都符合全部通過條件。

- [ ] **步驟 5：重新執行靜態驗證**

重跑 `quick_validate.py`。預期結束碼為 0。

---

### Task 4：最終檢查、安裝與安裝後複驗

**檔案：**

- 讀取：`skill-src/ai-short-drama-screenwriter/**`
- 建立：`C:\Users\user\.codex\skills\ai-short-drama-screenwriter\**`

**介面：**

- 輸入：已通過行為與靜態驗證的 skill 原始檔。
- 產出：Codex 個人 skills 目錄中的可探索 skill。

- [ ] **步驟 1：執行完整完成前檢查**

執行：

```powershell
rg -n 'TBD|TODO|FIXME|PLACEHOLDER|待定|稍後補' `
  'C:\Users\user\Downloads\AI Drama\skill-src\ai-short-drama-screenwriter'
```

預期：沒有輸出。

再確認 `SKILL.md` 能連到三個 references，`openai.yaml` 的顯示名稱、簡介、預設提示與 policy 正確，且所有測試情境已有通過證據。

- [ ] **步驟 2：確認安裝目標沒有既有 skill**

執行：

```powershell
Test-Path -LiteralPath 'C:\Users\user\.codex\skills\ai-short-drama-screenwriter'
```

預期：`False`。若為 `True`，停止並檢查既有內容；未取得使用者同意前不得覆寫。

- [ ] **步驟 3：取得授權後複製到正式位置**

執行：

```powershell
Copy-Item `
  -LiteralPath 'C:\Users\user\Downloads\AI Drama\skill-src\ai-short-drama-screenwriter' `
  -Destination 'C:\Users\user\.codex\skills\ai-short-drama-screenwriter' `
  -Recurse
```

此命令寫入工作區外，必須使用明確的檔案系統升級授權。

- [ ] **步驟 4：從安裝目錄執行新鮮驗證**

執行：

```powershell
& 'C:\Users\user\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  'C:\Users\user\.codex\skills\.system\skill-creator\scripts\quick_validate.py' `
  'C:\Users\user\.codex\skills\ai-short-drama-screenwriter'
```

預期：結束碼為 0。

再執行：

```powershell
Get-ChildItem -Recurse -File `
  'C:\Users\user\.codex\skills\ai-short-drama-screenwriter' |
  Select-Object FullName,Length
```

預期：列出 `SKILL.md`、`agents/openai.yaml`、`references/workflow.md`、`references/format.md` 與 `references/checklists.md`，且每個檔案大小大於 0。

- [ ] **步驟 5：回報安裝狀態與重新整理方式**

只有在任務 3 全部情境通過、安裝目錄的 `quick_validate.py` 結束碼為 0、五個必要檔案存在且非空時，才回報安裝完成。若目前工作中的 Codex 視窗未即時重新載入個人 skill 清單，說明重新開啟新任務或重新啟動 Codex 後即可看到 `$ai-short-drama-screenwriter`。

---

## 計畫自我檢查

- 規格涵蓋：完整流程、單點入口、繁體中文、格式、審閱、範圍界線、時效性資訊、安裝與驗證皆有對應任務。
- 占位掃描：計畫不含待補實作內容；測試結果檔的固定欄位是執行紀錄格式，不是未定需求。
- 介面一致：技術名稱、目錄名稱、顯示名稱、reference 路徑與安裝位置在所有任務中一致。
- 權限一致：工作區內建立與測試；只有最終安裝步驟要求工作區外寫入授權。
