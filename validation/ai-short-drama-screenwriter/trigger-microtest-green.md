# Trigger Micro-test GREEN 輸出

測試方式：每個 fresh-context 代理只能讀取當時的來源 `skill-src/ai-short-drama-screenwriter/SKILL.md`，只收到六個請求和固定表格欄位；未收到期望答案、其他輸出或其他工作區內容。設定皆為 `model=gpt-5.6-luna`、`reasoning_effort=medium`、`fork_turns=none`。

首次 GREEN 五份輸出在新增三項指定路由文字後取得；其中 E 有兩份誤走一般審閱／修改路由，故將該條目最小化限定為「不含單點創作」，並以全新代理重跑整組。最終通過組為下方 rerun 五份。

## 首次 GREEN：/root/final_fix_wave/green_microtest_1

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應的集數結構階段 | 先確立集數結構，再交付八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交一般小說／長篇小說對白編修 skill | 直接轉交小說編修流程 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交 AI 導演分鏡／逐鏡頭 storyboard skill | 先解析定稿劇本，再製作分鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance 影片提示詞 skill | 依 Seedance 格式直接產出 15 秒提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/workflow.md` 對應臺詞階段，必要時讀 `references/format.md` | 只交付改寫後三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 先讀 `references/workflow.md` 與 `references/format.md`；後續轉交 AI 導演分鏡／逐鏡頭 storyboard skill | 先完成第一集劇本，再銜接製作逐鏡分鏡 |

## 首次 GREEN：/root/final_fix_wave/green_microtest_2

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應的結構階段 | 先確立簡報，再寫八集大綱與各集鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交一般小說編修／對話潤飾 skill | 先確認小說語境，再修訂對話 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／Storyboard skill | 先分析定稿劇本，再拆解逐鏡分鏡 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞 skill | 先確認時長與素材，再撰寫影片提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/checklists.md`；需要格式判斷時讀取 `references/format.md` | 直接交付改寫後三句臺詞，不附分析 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 先讀取 `references/workflow.md` 與 `references/format.md`，再轉接導演分鏡／Storyboard skill | 先完成第一集劇本，再製作逐鏡分鏡 |

## 首次 GREEN：/root/final_fix_wave/green_microtest_3

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應的集數／結構階段；依指定以英文交付 | 先確立簡報與整體結構，再產出八集大綱及集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交長篇小說／一般文學對白編修類 skill | 直接由該類 skill 處理，不走本 skill 流程 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交 AI 導演分鏡／逐鏡頭 storyboard 類 skill | 直接分析既有劇本，再產出分鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞類 skill | 直接依 Seedance 規格產出 15 秒提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/checklists.md` 的修改／對白檢查項；不需額外讀 `format.md` | 直接改寫三句臺詞，只交付改寫結果 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 劇本部分讀取 `references/workflow.md` 與 `references/format.md`；分鏡部分轉交 AI 導演分鏡類 skill | 先完成第一集劇本，再以完成稿銜接製作逐鏡分鏡 |

## 首次 GREEN：/root/final_fix_wave/green_microtest_4

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 適用 | 讀取 `references/workflow.md` 的結構階段 | 先寫八集大綱，再設計各集集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 不適用 | 轉交小說編輯／長篇小說對白潤色類 skill | 直接進行小說對白潤色 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 不適用 | 轉交 AI 導演分鏡／逐鏡頭拆解類 skill | 先由分鏡 skill 解析定稿劇本，再交付分鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 不適用 | 轉交 Seedance／AI 影片提示詞類 skill | 直接撰寫 15 秒影片生成提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 適用 | 讀取 `references/workflow.md` 的臺詞階段 | 直接交付改寫後三句臺詞，不附分析 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 部分適用 | 劇本部分讀取 `references/workflow.md` 與 `references/format.md`；分鏡部分轉交 AI 導演分鏡類 skill | 先完成第一集劇本，再將完成稿轉為逐鏡分鏡 |

## 首次 GREEN：/root/final_fix_wave/green_microtest_5

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應結構階段 | 先確立創作簡報，再交付 8 集大綱及各集鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交一般小說／對白潤飾 skill | 直接進行小說對白潤飾 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／逐鏡拆解 skill | 直接依定稿劇本製作逐鏡分鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞 skill | 直接產出 15 秒影片生成提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/workflow.md` 對應臺詞階段 | 只交付改寫後的三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 先讀取 `references/workflow.md`；完成劇本後轉交導演分鏡 skill | 先交付第一集劇本，再銜接逐鏡分鏡 |

## 最終 GREEN rerun：/root/final_fix_wave/green_rerun_1

請求｜是否適用｜讀取哪個 reference／轉交哪類 skill｜交付順序
---|---|---|---
A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode.｜是｜讀取 `references/workflow.md` 的結構階段｜先定義整體結構，再逐集寫大綱與集尾鉤子
B. Polish the dialogue between two characters in my 120,000-word fantasy novel.｜否｜轉交一般小說／對白編修 skill｜由小說編修 skill 直接處理
C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。｜否｜轉交 AI 導演分鏡 skill｜由分鏡 skill 直接拆解
D. 為 Seedance 寫一段 15 秒影片生成提示詞。｜否｜轉交 Seedance／AI 影片提示詞 skill｜由影片提示詞 skill 直接產出
E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。｜是｜讀取 `references/workflow.md` 的臺詞／修改階段｜只交付改寫後三句臺詞
F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。｜部分適用｜先讀 `references/workflow.md` 與 `references/format.md`；後轉交 AI 導演分鏡 skill｜先完成第一集劇本，再將完成稿轉為逐鏡分鏡

## 最終 GREEN rerun：/root/final_fix_wave/green_rerun_2

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應的結構階段 | 先建立創作簡報，再交付八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交一般小說編輯／文字潤飾類 skill | 由該 skill 直接處理 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／Storyboard 類 skill | 由該 skill 讀取劇本後交付逐鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞類 skill | 由該 skill 直接產出提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/workflow.md` 的臺詞階段 | 只交付改寫後三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 劇本部分讀取 `references/workflow.md` 與 `references/format.md`；分鏡部分轉交導演分鏡類 skill | 先完成第一集劇本，再銜接逐鏡分鏡 |

## 最終 GREEN rerun：/root/final_fix_wave/green_rerun_3

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應的結構／集數階段 | 先確立集數結構，再交付英文八集大綱與集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交長篇小說／一般文本編修 skill | 由長篇小說編修 skill 直接處理對白潤色 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交導演分鏡／逐鏡頭 storyboard skill | 直接分析定稿劇本，再交付逐鏡頭分鏡表 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞 skill | 先確認 15 秒目標與素材，再交付 Seedance 提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/workflow.md` 對應的臺詞階段 | 只交付改寫後三句臺詞，不附分析 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 先讀取 `references/workflow.md` 與 `references/format.md`，再轉交導演分鏡 skill | 先完成第一集劇本，再將完成稿轉為逐鏡分鏡 |

## 最終 GREEN rerun：/root/final_fix_wave/green_rerun_4

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md` 對應的結構階段 | 先確立大綱，再逐集配置集尾鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 轉交長篇小說／對白潤飾類 skill | 直接交由長篇小說編修流程處理 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交 AI 導演分鏡／逐鏡拆解類 skill | 直接進行劇本至分鏡轉換 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／AI 影片提示詞類 skill | 直接撰寫 15 秒影片提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/workflow.md` 對應的臺詞階段；必要時讀取 `references/format.md` | 只交付改寫後三句臺詞 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 先讀 `references/workflow.md` 對應階段與 `references/format.md`，再轉交 AI 導演分鏡類 skill | 先完成劇本，再製作逐鏡分鏡 |

## 最終 GREEN rerun：/root/final_fix_wave/green_rerun_5

| 請求 | 是否適用 | 讀取哪個 reference／轉交哪類 skill | 交付順序 |
|---|---|---|---|
| A. Write an English 8-episode vertical short drama outline with a hook at the end of each episode. | 是 | 讀取 `references/workflow.md`；必要時讀取 `references/format.md` | 先確立創作簡報，再交付八集大綱與各集鉤子 |
| B. Polish the dialogue between two characters in my 120,000-word fantasy novel. | 否 | 不讀本 skill；轉交一般小說／對白編修類 skill | 直接進行小說對白編修 |
| C. 把既有定稿劇本轉成逐鏡頭導演分鏡表。 | 否 | 轉交 AI 導演分鏡／storyboard skill | 直接進行逐鏡頭拆解 |
| D. 為 Seedance 寫一段 15 秒影片生成提示詞。 | 否 | 轉交 Seedance／影片提示詞 skill | 直接產出 15 秒提示詞 |
| E. 只改寫這三句豎屏短劇臺詞，增加潛臺詞，不要分析。 | 是 | 讀取 `references/workflow.md` 的對應單點創作階段 | 只交付改寫後三句臺詞，不附分析 |
| F. 先寫第一集豎屏短劇劇本，再把完成劇本做成逐鏡分鏡。 | 是 | 先讀取 `references/workflow.md` 與 `references/format.md`；後續轉交 AI 導演分鏡／storyboard skill | 先完成第一集劇本，再銜接逐鏡分鏡 |
