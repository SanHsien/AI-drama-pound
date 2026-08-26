# Trigger Micro-test RED 控制輸出

測試方式：五個 fresh-context 代理，各自只能讀取當時的來源 `skill-src/ai-short-drama-screenwriter/SKILL.md`，只收到六個請求和固定表格欄位；未收到期望答案、其他輸出或其他工作區內容。設定皆為 `model=gpt-5.6-luna`、`reasoning_effort=medium`、`fork_turns=none`。

## /root/final_fix_wave/red_microtest_1

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 完整專案：讀取 `references/workflow.md` | 先確立創作簡報，再產出八集大綱與各集鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交小說／長篇文學編修類 skill | 直接由適合的小說編修 skill 處理 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／逐鏡頭拆解類 skill | 直接進行劇本轉分鏡 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞類 skill | 直接撰寫 15 秒提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 單點創作；不需讀取 reference | 只交付改寫後的三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 部分適用 | 劇本撰寫：讀取 `references/format.md`；分鏡部分轉交導演分鏡類 skill | 先完成第一集劇本，再將定稿劇本轉為逐鏡分鏡 |

## /root/final_fix_wave/red_microtest_2

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md`；短劇編劇完整專案 | 先確立創作簡報，再產出八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交一般小說／長篇文本修訂類 skill | 直接轉交 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／Storyboard 類 skill | 直接轉交 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞類 skill | 直接轉交 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/checklists.md`；短劇臺詞修改 | 只交付改寫後三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 部分適用 | 劇本階段讀取 `references/format.md`；分鏡階段轉交導演分鏡類 skill | 先完成第一集劇本，再轉成逐鏡分鏡表 |

## /root/final_fix_wave/red_microtest_3

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 適用 | 完整專案，讀取 `references/workflow.md` | 先確立創作簡報，再產出八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 不適用 | 轉交長篇小說／一般小說對白編修 skill | 直接轉交 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 不適用 | 轉交 AI 導演分鏡／逐鏡頭 storyboard skill | 直接轉交 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 不適用 | 轉交 Seedance／AI 影片提示詞 skill | 直接轉交 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 適用 | 單點創作，不需讀取 reference | 直接改寫三句臺詞，不附分析 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 部分適用 | 先讀 `references/format.md`；完成劇本後轉交 AI 導演分鏡 skill | 先寫第一集劇本，再製作逐鏡分鏡 |

## /root/final_fix_wave/red_microtest_4

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 單點創作；不需額外 reference | 直接交付八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交長篇小說編修／對白潤飾類 skill | 由小說編修 skill 處理 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／Storyboard 類 skill | 由分鏡 skill 直接處理 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞類 skill | 由 Seedance skill 處理 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 單點創作；不需額外 reference | 只交付改寫後三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 部分適用 | 先讀 `references/format.md`；後轉交導演分鏡／Storyboard 類 skill | 先完成第一集劇本，再交接並製作逐鏡分鏡 |

## /root/final_fix_wave/red_microtest_5

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` | 先創作簡報，再完成八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交長篇小說／文學編輯 skill | 直接處理小說對白潤飾 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／逐鏡拆解 skill | 先分析定稿劇本，再交付分鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞 skill | 直接產出 15 秒提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 不需讀取 reference；屬單點臺詞改寫 | 只交付改寫後三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 部分適用 | 先讀取 `references/format.md`；後轉交導演分鏡／逐鏡拆解 skill | 先完成第一集劇本，再製作逐鏡分鏡 |
