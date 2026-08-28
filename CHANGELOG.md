[English](CHANGELOG.en.md) | 中文版

# 變更紀錄

格式參考 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，新的在上面。
本檔只記錄**本 fork 的維護歷史**（2026-08-28 起）；上游
[`POUND0423/AI-drama-pound`](https://github.com/POUND0423/AI-drama-pound)
的產品演進見其自身歷史與 [`docs/UPSTREAM.md`](docs/UPSTREAM.md) 的審查清冊。
逐筆採用／略過的理由記在 [`docs/DECISIONS.md`](docs/DECISIONS.md)。

---

## 2026-08-28（覆核）

### 修復

- **`.gitignore` 不擋 cookie／憑證／本機劇本草稿。** 加入 `cookies.txt`、`cookies.json`、`credentials.json`、`/drafts/`、`*.fountain`，並用 `git check-ignore` 測試鎖住。見 [`REVIEW.md`](REVIEW.md) R-01。

### 新增

- **`REVIEW.md`。** 第一次專案覆核快照，補上 overlay 首推後的 CI／CodeQL URL。

## 2026-08-28

### 新增

- **Windows-first 維護骨架。** `AGENTS.md`、`CLAUDE.md`、`FORK.md`、`NOTICE.md`、
  `CONTRIBUTING.md`、`SECURITY.md`、`CODE_OF_CONDUCT.md`、`docs/`、`tools/` 維護腳本、
  `tests/`、`.github/` 的 CI／CodeQL／Dependabot／上游檢查／相依新鮮度。
  CI 跑 Ubuntu 3.9–3.14 與 Windows 3.14：pytest、ruff（E9+F）、`validate_skills.py`、
  相對連結檢查。
- **公開入口只留繁中與英文。** `README.md` 維持繁中主檔、`README.en.md` 為英文鏡像。
  來源與授權 credit 保留，作者宣傳不轉載。
