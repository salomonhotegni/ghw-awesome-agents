# Sidekick - My First Agent

A fun, friendly, and upbeat personal chatbot agent built using the Backboard SDK.

## Overview

Sidekick is an AI-powered chatbot that serves as your personal assistant. It's warm, playful, and genuinely helpful while being able to remember useful facts and preferences you share during conversations.

## Features

- **Persistent Assistant**: The assistant ID is persisted in `sidekick.json` for consistent conversations
- **Stateful Conversations**: Remembers facts and preferences from previous interactions
- **User-Friendly**: Designed to be warm, playful, and naturally helpful
- **Backboard Integration**: Built on the Backboard SDK for reliable AI assistant functionality

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
python sidekick.py
```

## Files

- **sidekick.py**: Main agent implementation
- **sidekick.json**: State file storing the assistant ID
- **requirements.txt**: Python dependencies
- **README.md**: This file

## Dependencies

- `backboard-sdk==1.5.15`: Backboard SDK for AI assistant management

## How It Works

1. The agent loads or creates an assistant on first run
2. The assistant ID is stored in `sidekick.json` for persistence
3. Subsequent runs use the same assistant, maintaining conversation history
4. The agent uses a system prompt that defines Sidekick's personality and behavior

## Configuration

The agent's personality is defined by the `SYSTEM_PROMPT` in `sidekick.py`. You can customize this prompt to adjust Sidekick's tone and behavior.

## License

See the main project repository for license information.
