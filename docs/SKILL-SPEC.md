# 產品 Skill 規格（本 fork 摘要）

完整寫作指引以上游 `skill-src/ai-short-drama-screenwriter/SKILL.md` 與 [Agent Skills 規格](https://agentskills.io/specification.md) 為準。本檔只鎖定本 fork 驗收會檢查的契約。

## 目錄

```text
skill-src/<skill-name>/
├── SKILL.md        # 必填；主指令，建議 <500 行
├── agents/         # 可選；Codex 顯示名稱與隱式啟動
├── references/     # 可選；按需載入
├── scripts/        # 可選
└── assets/         # 可選
```

`name` 必須與目錄名完全相同。目前唯一產品 skill 是 `ai-short-drama-screenwriter`。

## Frontmatter

```yaml
---
name: skill-name
description: What this skill does and when to use it. Include trigger phrases.
---
```

| 欄位 | 必填 | 限制 |
|---|---|---|
| `name` | 是 | 1–64 字元，小寫 `a-z`、數字、連字號。不可開頭／結尾為連字號，不可連續 `--`，必須等於目錄名 |
| `description` | 是 | 1–1024 字元；寫清做什麼、何時觸發 |
| `license` | 否 | 預設 MIT |
| `metadata` | 否 | `version` 放這裡，不要放成 top-level `version` |

## 寫作邊界

- 產品語言維持上游原文（目前為繁體中文）。
- 不要在 `SKILL.md` 加入 Claude Code 專用的 `` !`command` ``；那會讓其他宿主看到字面字串。
- 使用者只要劇本時，不輸出分鏡或影片模型提示詞。
- 不提交憑證或使用者劇本。

本 fork 的 `tools/validate_skills.py` 檢查：每個 `skill-src/*/` 都有 `SKILL.md`、frontmatter 存在、`name` 符合目錄與格式、`description` 長度合法。警告（缺 trigger 用語、超過 500 行）不會讓 gate 失敗。
