# AI 短劇編劇

> 以繁體中文完成短篇／豎屏短劇的選題、結構、角色、分場、臺詞、衝突、反轉、格式與修改。

[GitHub Release v0.1.0](https://github.com/POUND0423/AI-drama-pound/releases/tag/v0.1.0) · [MIT License](LICENSE)

`ai-short-drama-screenwriter` 是一個可供 ChatGPT 桌面版 Codex、Codex CLI 與 IDE extension 使用的 standalone skill。它把故事前提與製作限制整理成可見、可聽、可拍攝，且有明確戲劇推進的短劇內容。

## 專案解決什麼問題

一般 AI 短劇草稿常見以下問題：

- 故事只有概念，缺乏可持續推進的角色目標、阻力與代價。
- 角色轉變沒有前置事件，人物動機在場次間跳躍。
- 臺詞只解說背景，缺少試探、迴避、反應與潛臺詞。
- 反轉沒有前文線索，集尾只中斷事件而沒有下一步問題。
- 場次缺少內外景、地點或時間，難以直接進入製作。
- 使用者只要求劇本，輸出卻越界加入分鏡或影片模型提示詞。

本技能用明確的任務路由、八階段編劇流程、標準短劇格式與修改清單，讓輸出保持可拍性、敘事推進與交付範圍一致。

## 主要功能

- **完整編劇流程**：創作簡報、題材定位、全劇與單集結構、角色關係、分場、臺詞、衝突／情緒／反轉／鉤子、初稿與修改。
- **單點創作**：只處理指定的選題、結構、角色、分場、臺詞、衝突、反轉或格式，不強制重做完整專案。
- **標準短劇格式**：支援場次、內景／外景、地點、時間、動作、角色名稱、臺詞及畫面文字。
- **劇本審閱與修改**：按影響程度提供問題、段落證據、造成的影響與可執行修正方向。
- **限制保持**：保留使用者指定的集數、時長、觀眾、類型、平台、預算、場景與交付形式。
- **繁體中文輸出**：預設使用繁體中文；其他語言可在提示中指定。
- **跨技能銜接**：混合需求先完成劇本，再銜接環境中已安裝且適用的分鏡或影片提示詞技能。

## 安裝方法

### 前置條件

- 已安裝 [Git](https://git-scm.com/)。
- 已安裝支援 standalone skills 的 ChatGPT 桌面版 Codex、Codex CLI 或 IDE extension。

Codex 的個人技能位置為 `$HOME/.agents/skills`。每個技能都必須是獨立資料夾，且資料夾內直接包含 `SKILL.md`。詳見 [OpenAI 官方技能文件](https://learn.chatgpt.com/docs/build-skills)。

### Windows PowerShell

```powershell
git clone --depth 1 https://github.com/POUND0423/AI-drama-pound.git

$repoPath = Join-Path (Get-Location) 'AI-drama-pound'
$skillPath = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.agents\skills\ai-short-drama-screenwriter'

New-Item -ItemType Directory -Force -Path $skillPath | Out-Null
Copy-Item -Path (Join-Path $repoPath 'skill-src\ai-short-drama-screenwriter\*') -Destination $skillPath -Recurse -Force

Test-Path (Join-Path $skillPath 'SKILL.md')
```

最後一行應輸出 `True`。

### macOS／Linux

```bash
git clone --depth 1 https://github.com/POUND0423/AI-drama-pound.git

mkdir -p "$HOME/.agents/skills/ai-short-drama-screenwriter"
cp -R "AI-drama-pound/skill-src/ai-short-drama-screenwriter/." \
  "$HOME/.agents/skills/ai-short-drama-screenwriter/"

test -f "$HOME/.agents/skills/ai-short-drama-screenwriter/SKILL.md" \
  && echo "Skill installed"
```

成功時會輸出 `Skill installed`。Codex 通常會自動偵測技能；若沒有出現，請重新啟動 Codex。

## 使用方法

### 顯式呼叫

在提示中直接加入技能名稱：

```text
使用 $ai-short-drama-screenwriter，把以下故事前提規劃成 8 集、每集 90 秒的都市懸疑短劇。主要場景不超過 3 個；先提供創作簡報、角色關係、全劇節拍與第一集劇本。

故事前提：外送員每天替一位失憶老人送餐，最後發現老人可能是失蹤多年的外公。
```

### 隱式呼叫

也可以直接提出符合技能範圍的需求，例如：

```text
只修改這段短劇重逢戲的臺詞，增加潛臺詞，不要重做人物設定或全劇大綱。
```

技能允許隱式啟動；是否啟動取決於請求是否符合 `SKILL.md` 的使用範圍。

## 輸入輸出範例

### 輸入

```text
使用 $ai-short-drama-screenwriter，將「外送員替失憶老人送餐，逐漸發現老人是失蹤多年的外公」發展成 8 集都市懸疑短劇。每集 90 秒，主要場景不超過 3 個。請提供必要假設、創作簡報、角色關係、全劇節拍與第一集劇本。
```

### 輸出節錄

```text
必要假設
- 觀眾：偏好都市情感懸疑的短劇觀眾
- 製作限制：主要場景為外送站、老公寓與主角家

創作簡報
- 類型：都市溫情懸疑
- 主角目標：確認老人身分，同時查明家人隱瞞的往事
- 主要阻力：老人記憶破碎，主角母親阻止他繼續調查

角色關係
- 阿澤：外送員；從同情老人轉為追查自己的家族秘密
- 陳伯：失憶老人；保留與阿澤童年有關的零碎記憶
- 美玲：阿澤母親；知道老人身分，但害怕舊事再次傷害家人

全劇節拍（節錄）
- 第 1 集：阿澤在老人門口撿到自己童年的照片；母親要求他停止送餐。
- 第 4 集：老人短暫恢復記憶，叫出阿澤父親的名字。
- 第 8 集：阿澤確認血緣真相，必須決定公開秘密或保護母親。

第 1 集

1. 內景・老公寓走廊・夜

阿澤提著餐袋停在 302 室門前。門縫下壓著一張泛黃照片。

照片裡，五歲的阿澤坐在一名男子肩上。男子的臉被撕掉一半。

阿澤
陳伯，您的晚餐到了。

門內傳來老人顫抖的聲音。

陳伯（OS）
小澤，你終於回來了。

阿澤僵住。他從未告訴老人自己的小名。

切黑。
```

實際輸出會依故事前提、限制與指定交付形式改變，不保證與範例逐字相同。

## 功能邊界

- 只要求劇本時，不輸出逐鏡分鏡、景別、運鏡或 AI 影片模型參數。
- 本倉庫不包含分鏡或影片提示詞技能；混合交付需要環境中另有適用技能。
- 涉及當前平台偏好、演算法或市場趨勢時，必須先查證，不能把舊資訊當成現況。

## 專案結構

```text
AI-drama-pound/
├── skill-src/ai-short-drama-screenwriter/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
│       ├── workflow.md
│       ├── format.md
│       └── checklists.md
├── validation/ai-short-drama-screenwriter/
├── docs/superpowers/
├── LICENSE
└── README.md
```

## 驗證狀態

- [RED 基線測試](validation/ai-short-drama-screenwriter/baseline-results.md)：記錄沒有技能時的格式缺口。
- [GREEN 行為測試](validation/ai-short-drama-screenwriter/skill-results.md)：四個情境最終全部通過。
- [觸發邊界微測試](validation/ai-short-drama-screenwriter/trigger-microtest-results.md)：A–F 最終各為 5/5。
- 官方技能結構驗證：通過。

## 常見問題

### 安裝後找不到技能

確認以下檔案直接存在：

```text
$HOME/.agents/skills/ai-short-drama-screenwriter/SKILL.md
```

若路徑正確但技能仍未出現，重新啟動 Codex。

### 可以直接產生分鏡或影片提示詞嗎？

此技能本身負責短劇編劇。若同時要求劇本與分鏡或影片提示詞，它會先完成劇本，再嘗試銜接環境中已安裝的適用技能。

## 授權

本專案採用 [MIT License](LICENSE)。
