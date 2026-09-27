<div align="center">

# AI Short-Drama Screenwriter

### Topic selection, structure, characters, scenes, dialogue, conflict, reversals, format, and revision for short-form / vertical dramas in Traditional Chinese

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![CI](https://github.com/SanHsien/AI-drama-pound/actions/workflows/ci.yml/badge.svg)](https://github.com/SanHsien/AI-drama-pound/actions/workflows/ci.yml)
[![Upstream Release v0.1.0](https://img.shields.io/badge/upstream-v0.1.0-2ea44f.svg)](https://github.com/POUND0423/AI-drama-pound/releases/tag/v0.1.0)

<p>
  <a href="README.md">繁體中文</a> ·
  <a href="README.en.md"><strong>English</strong></a>
</p>

</div>

> **This is a Windows-first maintenance fork of [`POUND0423/AI-drama-pound`](https://github.com/POUND0423/AI-drama-pound).** It keeps the MIT license and full git history. Product behaviour follows upstream; this line adds an English entry, a Windows development gate, and commit-by-commit upstream review. See [`FORK.md`](FORK.md), [`docs/UPSTREAM.md`](docs/UPSTREAM.md), and [`NOTICE.md`](NOTICE.md).

`ai-short-drama-screenwriter` is a standalone skill for Codex, Claude Code, Cursor, and other hosts that support [Agent Skills](https://agentskills.io). It turns a story premise and production constraints into visible, audible, shootable short-drama material with a clear dramatic engine.

## What this project solves

Typical AI short-drama drafts fail in these ways:

- The story is only a concept, with no lasting character goal, obstacle, or cost.
- Character change has no preceding events; motives jump between scenes.
- Dialogue explains background instead of probing, dodging, reacting, or implying.
- Reversals have no earlier clues; episode endings interrupt events without a next question.
- Scenes omit interior/exterior, location, or time, so they cannot go into production.
- The user asked only for a script, but the output adds storyboards or video-model prompts.

The skill uses explicit task routing, an eight-stage writing process, a standard short-drama format, and revision checklists so the output stays shootable, dramatically advancing, and in scope.

## Features

- **Full writing process**: creative brief, topic framing, series and episode structure, character relationships, scenes, dialogue, conflict / emotion / reversals / hooks, draft and revision.
- **Single-point work**: handle only the requested topic, structure, character, scene, dialogue, conflict, reversal, or format — without rebuilding the whole project.
- **Standard short-drama format**: scene numbers, INT/EXT, location, time, action, character names, dialogue, and on-screen text.
- **Script review**: ranked issues with paragraph evidence, impact, and actionable fixes.
- **Constraint keeping**: preserve episode count, duration, audience, genre, platform, budget, locations, and delivery form.
- **Traditional Chinese by default**: other languages can be requested in the prompt.
- **Handoff to other skills**: mixed requests finish the script first, then hand off to an already-installed storyboard or video-prompt skill.

## Install

Copy `skill-src/ai-short-drama-screenwriter/` into the host skills directory. The rest of the repository is this fork's maintenance overlay — do not copy it into the skills folder.

| Host | Suggested path |
| --- | --- |
| Codex | `~\.agents\skills\ai-short-drama-screenwriter\` |
| Claude Code | `~\.claude\skills\ai-short-drama-screenwriter\` |
| Cursor | `~\.cursor\skills\ai-short-drama-screenwriter\` |

Each skill must be its own folder with `SKILL.md` at the top. See the [OpenAI skills docs](https://learn.chatgpt.com/docs/build-skills).

### Prerequisites

- [Git](https://git-scm.com/)
- A host that supports standalone skills (Codex, Claude Code, Cursor, or equivalent)

### Windows PowerShell

```powershell
git clone --depth 1 https://github.com/SanHsien/AI-drama-pound.git

$repoPath = Join-Path (Get-Location) 'AI-drama-pound'
$skillPath = Join-Path ([Environment]::GetFolderPath('UserProfile')) '.agents\skills\ai-short-drama-screenwriter'

New-Item -ItemType Directory -Force -Path $skillPath | Out-Null
Copy-Item -Path (Join-Path $repoPath 'skill-src\ai-short-drama-screenwriter\*') -Destination $skillPath -Recurse -Force

Test-Path (Join-Path $skillPath 'SKILL.md')
```

The last line should print `True`. For Cursor, change `$skillPath` to `~\.cursor\skills\ai-short-drama-screenwriter`.

### macOS / Linux

```bash
git clone --depth 1 https://github.com/SanHsien/AI-drama-pound.git

mkdir -p "$HOME/.agents/skills/ai-short-drama-screenwriter"
cp -R "AI-drama-pound/skill-src/ai-short-drama-screenwriter/." \
  "$HOME/.agents/skills/ai-short-drama-screenwriter/"

test -f "$HOME/.agents/skills/ai-short-drama-screenwriter/SKILL.md" \
  && echo "Skill installed"
```

On success this prints `Skill installed`. Restart the host if the skill does not appear.

## Usage

### Explicit

```text
Use $ai-short-drama-screenwriter to plan the following premise as an 8-episode urban-suspense short drama, 90 seconds per episode. Keep main locations to 3 or fewer. First deliver a creative brief, character relationships, series beats, and episode 1.

Premise: A delivery rider brings meals to an amnesiac elder every day, then realises the elder may be his long-missing grandfather.
```

### Implicit

```text
Only revise the dialogue in this short-drama reunion scene. Add subtext. Do not rebuild the character bible or series outline.
```

Implicit invocation is allowed; whether it fires depends on the request matching `SKILL.md`.

## Example

### Input

```text
使用 $ai-short-drama-screenwriter，將「外送員替失憶老人送餐，逐漸發現老人是失蹤多年的外公」發展成 8 集都市懸疑短劇。每集 90 秒，主要場景不超過 3 個。請提供必要假設、創作簡報、角色關係、全劇節拍與第一集劇本。
```

### Excerpted output

The skill's default output is Traditional Chinese. The excerpt below is the same sample as [`README.md`](README.md):

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

Actual output changes with the premise, constraints, and requested deliverable. It is not guaranteed to match this excerpt word for word.

## Boundaries

- When the user asks only for a script, do not emit shot lists, shot sizes, camera moves, or AI video-model parameters.
- This repository does not ship storyboard or video-prompt skills; mixed delivery needs another installed skill.
- Current platform preferences, algorithms, or market trends must be verified; do not treat stale notes as facts.

## Layout

```text
AI-drama-pound/
├── skill-src/ai-short-drama-screenwriter/   # product skill (follows upstream)
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
├── validation/ai-short-drama-screenwriter/  # upstream qualitative checks
├── docs/superpowers/                        # upstream design notes
├── AGENTS.md / FORK.md / NOTICE.md          # this fork's overlay
├── tools/ / tests/ / .github/               # Windows gate and CI
├── LICENSE
├── README.md
└── README.en.md
```

Development and acceptance commands: [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md). Maintainer clone:

```powershell
git clone https://github.com/SanHsien/AI-drama-pound.git
cd AI-drama-pound
python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements-dev.txt
pwsh -NoProfile -File tools\dev_check.ps1
```

## Upstream validation

- [RED baseline](validation/ai-short-drama-screenwriter/baseline-results.md): format gaps without the skill
- [GREEN behaviour](validation/ai-short-drama-screenwriter/skill-results.md): all four scenarios passed
- [Trigger microtests](validation/ai-short-drama-screenwriter/trigger-microtest-results.md): A–F each 5/5
- Official skill-structure check: passed

## FAQ

### The skill does not appear after install

Confirm this file exists:

```text
$HOME/.agents/skills/ai-short-drama-screenwriter/SKILL.md
```

If the path is correct and the skill still does not appear, restart the host.

### Can it emit storyboards or video prompts?

This skill writes short-drama scripts. If the request also asks for storyboards or video prompts, it finishes the script first, then tries to hand off to an already-installed applicable skill.

## License

[MIT License](LICENSE), forked from [`POUND0423/AI-drama-pound`](https://github.com/POUND0423/AI-drama-pound). Attribution: [`NOTICE.md`](NOTICE.md).
