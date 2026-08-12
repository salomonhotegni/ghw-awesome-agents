# GHW Awesome Agents ([Global Hack Week: Agents Week](https://ghw.mlh.com/schedule))

> A growing collection of focused AI agents and applications built for [MLH Global Hack Week: Agents Week](https://ghw.mlh.com/schedule).

This repository brings my Global Hack Week agent challenges into one place. Each project is independently usable, tested, and maintained in its own GitHub repository; this collection pins a known version of every project with Git submodules.

## Projects

| Project | Challenge | What it does | AI mode |
|---|---|---|---|
| [LabCouncil](https://github.com/salomonhotegni/final-boss) | Challenge 6: Final Boss | Coordinates five specialist agents to turn a research idea into a reviewed experiment plan and scored decision. | Backboard required; five persistent assistants |
| [Git Helper Agent](https://github.com/salomonhotegni/git-helper-agent) | Build a Git Commit & PR Agent | Turns local Git diffs into concise Conventional Commit messages and ready-to-paste pull request summaries. | Offline by default; optional Backboard refinement |
| [Terminal AI Helper](https://github.com/salomonhotegni/terminal-ai-helper) | Build a Terminal AI Helper | Turns plain English into a reviewed terminal command, explains its risk, and asks before running it. | Backboard required |
| [Long-Term Memory Agent](https://github.com/salomonhotegni/long-term-memory-agent) | Give Your Agent Long-Term Memory | Remembers preferences and completed interactions across separate sessions with a transparent local SQLite database. | Backboard required for replies; memory management works offline |
| [Human-in-the-Loop Agent](https://github.com/salomonhotegni/human-in-the-loop-agent) | Build a Human-in-the-Loop Workflow | Pauses for explicit human approval before sensitive actions like emails or purchases, while safe requests run automatically. | Backboard required for planning; approval gate is enforced locally |

## Get started

Clone the collection and initialize every agent in one command:

```bash
git clone --recurse-submodules \
  https://github.com/salomonhotegni/ghw-awesome-agents.git
cd ghw-awesome-agents
```

If you already cloned the repository without its submodules, initialize them with:

```bash
git submodule update --init --recursive
```

Each directory under `agents/` is a complete project pinned to a tested commit. Follow the README inside an agent for its full setup, usage, safety notes, and development workflow.

## Try the agents

Run each example from the collection root.

### LabCouncil

Requirements: Python 3.10+ and a Backboard API key. LabCouncil streams a five-agent research-design workflow through a local Flask interface.

```bash
cd agents/final-boss
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export BACKBOARD_API_KEY="your-api-key"
python app.py
```

Open <http://127.0.0.1:5000>. The Research Scientist, Skeptical Reviewer, Experimentalist, Resource Manager, and Program Chair collaborate to produce a seven-section report and final decision. See the [LabCouncil documentation](https://github.com/salomonhotegni/final-boss) for its workflow and API.

### Git Helper Agent

Requirements: Python 3.10+ and Git. Its deterministic generator works locally without an API key.

```bash
cd agents/git-helper-agent
python -m pip install -e .
git-helper commit --diff-file examples/sample.diff
```

Example output:

```text
feat(diff-parser): add rename parsing

- Update 1 source file
- Update 1 test file
```

The optional Backboard provider adds AI refinement while keeping offline output as the safe default. See the [project documentation](https://github.com/salomonhotegni/git-helper-agent#optional-ai-refinement) for setup.

### Terminal AI Helper 

Requirements: Python 3.10+, the Backboard SDK, and a `BACKBOARD_API_KEY` environment variable.

```bash
cd agents/terminal-ai-helper
python -m pip install -r requirements.txt
export BACKBOARD_API_KEY="your-api-key"
python terminal_helper.py --dry-run "Find all files larger than 100MB"
```

PowerShell users can set the key with:

```powershell
$env:BACKBOARD_API_KEY = "your-api-key"
```

`--dry-run` still asks Backboard to generate the command, but it never offers to execute it. In normal mode, confirmation defaults to **No**, and commands classified as high risk require typing `RUN` exactly.

### Long-Term Memory Agent

Requirements: Python 3.10+, the Backboard SDK, and a `BACKBOARD_API_KEY` environment variable. SQLite is included with Python and requires no separate database server.

```bash
cd agents/long-term-memory-agent
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export BACKBOARD_API_KEY="your-api-key"
python memory_agent.py --remember "I prefer concise answers and Python examples."
python memory_agent.py "How should you explain decorators to me?"
```

The first command saves a preference locally without calling Backboard. The second starts a separate process, reloads that preference from SQLite, and uses it to personalize the AI response. Run `python memory_agent.py` for interactive chat, or inspect and manage local data with `--memories`, `--history`, `--forget`, and `--clear`.

## Repository structure

```text
ghw-awesome-agents/
├── .gitmodules
├── README.md
└── agents/
    ├── final-boss/             # Five-agent research council
    ├── git-helper-agent/       # Git commit and PR summaries
    ├── long-term-memory-agent/ # SQLite-backed persistent memory
    └── terminal-ai-helper/     # English-to-terminal commands
```

Why submodules?

- Every agent keeps its own history, releases, issues, tests, and README.
- The collection records the exact commit that was reviewed together.
- Each agent can be cloned and used independently.

## Run the tests

The agents have separate environments and test commands.

LabCouncil:

```bash
cd agents/final-boss
python -m pip install -r requirements.txt
python -m pytest -q
```

Git Helper Agent:

```bash
cd agents/git-helper-agent
python -m pip install -e ".[dev]"
python -m pytest -q
```

Terminal AI Helper:

```bash
cd agents/terminal-ai-helper
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Long-Term Memory Agent:

```bash
cd agents/long-term-memory-agent
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The test suites mock external AI calls and do not require live Backboard requests.

## Add or update an agent

Add a published agent repository:

```bash
git submodule add \
  https://github.com/salomonhotegni/NEW-AGENT.git \
  agents/NEW-AGENT
git add .gitmodules agents/NEW-AGENT
```

When updating an existing agent, commit and push inside the agent repository first. Then record its new pinned commit in this collection:

```bash
git add agents/AGENT-NAME
git commit -m "chore: update AGENT-NAME"
```

## License

Licensing is defined by each independent project. Check the corresponding repository for its license terms before reuse; Git Helper Agent, Terminal AI Helper, and Long-Term Memory Agent include MIT licenses.
