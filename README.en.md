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

See the Traditional Chinese [`README.md`](README.md) for a full sample input and excerpted output. Actual output changes with the premise, constraints, and requested deliverable.

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

- [RED baseline](validation/ai-short-drama-screenwriter/baseline-results.md)
- [GREEN behaviour](validation/ai-short-drama-screenwriter/skill-results.md)
- [Trigger microtests](validation/ai-short-drama-screenwriter/trigger-microtest-results.md)

## License

[MIT License](LICENSE), forked from [`POUND0423/AI-drama-pound`](https://github.com/POUND0423/AI-drama-pound). Attribution: [`NOTICE.md`](NOTICE.md).
