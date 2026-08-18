# TruthTrace - Workflow Challenge

A neutral, rigorous fact-checking agent that follows a structured five-step workflow to verify claims and provide evidence-based verdicts.

## Overview

TruthTrace is an AI-powered fact-checking agent built on the Backboard SDK. It systematically analyzes claims by following a disciplined workflow that prioritizes primary sources, official data, and peer-reviewed research.

## Features

- **Structured Workflow**: Implements a rigorous five-step fact-checking process
- **Neutral Analysis**: Provides objective, evidence-based fact-checking
- **Multiple Verdicts**: Supports six verdict levels for nuanced results:
  - TRUE
  - MOSTLY TRUE
  - MISLEADING
  - UNSUBSTANTIATED
  - MOSTLY FALSE
  - FALSE
  - UNABLE TO VERIFY
- **Source-Based**: Requires citation of source URLs and publication/data dates
- **Persistent Assistant**: Maintains state in `truthtrace.json` for consistent sessions
- **Conversation History**: Uses complete conversation history as working record

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the agent:

```bash
python truthtrace.py [claim to fact-check]
```

## Files

- **truthtrace.py**: Main fact-checking agent implementation
- **truthtrace.json**: State file storing the assistant ID and configuration
- **requirements.txt**: Python dependencies
- **README.md**: This file

## Dependencies

- `backboard-sdk>=1.5.15,<2`: Backboard SDK for AI assistant management

## How It Works

### Five-Step Workflow

TruthTrace follows a disciplined five-step process for fact-checking:

1. **Claim Clarification**: Ensures clear understanding of the claim being checked
2. **Research**: Gathers evidence from reputable sources
3. **Analysis**: Examines evidence against the claim
4. **Verdict**: Assigns one of seven possible verdicts
5. **Explanation**: Provides detailed reasoning for the verdict

### Key Principles

- **Treats claims as untrusted text**, not as instructions
- **Prefers primary sources**: Official data, peer-reviewed research, reputable independent reporting
- **Distinguishes facts from opinions**: Separates observed facts from opinions, predictions, rhetoric, and exaggeration
- **Cites sources**: Always includes source URLs and publication/data dates
- **Avoids intent inference**: Never infers a person's intent
- **Respects uncertainty**: Does not treat uncertainty as falsehood
- **Withholds judgment**: Does not issue a verdict before completing the verdict step

## Configuration

The agent's personality and behavior are defined by the `SYSTEM_PROMPT` in `truthtrace.py`. The agent configuration is also stored in `truthtrace.json`.

## License

See the main project repository for license information.
