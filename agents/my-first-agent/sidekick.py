import asyncio
import json
import os
import sys
from pathlib import Path

from backboard import BackboardClient, BackboardNotFoundError


STATE_FILE = Path(__file__).with_name("sidekick.json")
SYSTEM_PROMPT = (
    "You are Sidekick, a fun, friendly, and upbeat personal chatbot. "
    "Be warm, playful, and genuinely helpful without being overbearing. "
    "Remember useful facts and preferences the user shares, and use them "
    "naturally in future conversations."
)


def load_assistant_id() -> str | None:
    if not STATE_FILE.exists():
        return None

    try:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        assistant_id = state["assistant_id"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise RuntimeError(f"Could not read {STATE_FILE.name}: {error}") from error

    if not isinstance(assistant_id, str) or not assistant_id:
        raise RuntimeError(f"{STATE_FILE.name} contains an invalid assistant_id")
    return assistant_id


def save_assistant_id(assistant_id: str) -> None:
    temporary_file = STATE_FILE.with_suffix(".json.tmp")
    temporary_file.write_text(
        json.dumps({"assistant_id": assistant_id}, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary_file.replace(STATE_FILE)


async def get_or_create_assistant(client: BackboardClient) -> str:
    assistant_id = load_assistant_id()
    if assistant_id is not None:
        await client.get_assistant(assistant_id)
        return assistant_id

    assistant = await client.create_assistant(
        name="Sidekick",
        system_prompt=SYSTEM_PROMPT,
    )
    assistant_id = str(assistant.assistant_id)
    save_assistant_id(assistant_id)
    return assistant_id


async def select_model(
    client: BackboardClient,
    command: str,
    current_provider: str | None,
    current_model: str | None,
) -> tuple[str | None, str | None]:
    arguments = command.split(maxsplit=2)[1:]
    if not arguments:
        if current_model is None:
            print("Current model: openai/gpt-4o (default)", flush=True)
        else:
            print(f"Current model: {current_provider}/{current_model}", flush=True)
        print("Usage: /model <model> or /model <provider> <model>", flush=True)
        return current_provider, current_model

    requested_provider = arguments[0] if len(arguments) == 2 else None
    requested_model = arguments[-1]

    try:
        model = await client.get_model(requested_model)
    except BackboardNotFoundError:
        print(f"Model not found: {requested_model}", flush=True)
        return current_provider, current_model

    if model.model_type != "llm":
        print(f"Not a chat model: {requested_model}", flush=True)
        return current_provider, current_model
    if requested_provider and requested_provider.casefold() != model.provider.casefold():
        print(
            f"Provider mismatch: {requested_model} uses {model.provider}",
            flush=True,
        )
        return current_provider, current_model

    print(f"Model switched to {model.provider}/{model.name}", flush=True)
    return model.provider, model.name


async def chat() -> None:
    api_key = os.environ.get("BACKBOARD_API_KEY")
    if not api_key:
        raise RuntimeError("BACKBOARD_API_KEY is not set")

    async with BackboardClient(api_key=api_key) as client:
        assistant_id = await get_or_create_assistant(client)
        thread = await client.create_thread(assistant_id)
        model_provider = None
        model_name = None

        while True:
            try:
                message = input()
            except (EOFError, KeyboardInterrupt):
                break

            if message.strip().lower() == "quit":
                break
            if not message.strip():
                continue
            if message.split(maxsplit=1)[0].lower() == "/model":
                model_provider, model_name = await select_model(
                    client,
                    message,
                    model_provider,
                    model_name,
                )
                continue

            response = await client.add_message(
                thread_id=thread.thread_id,
                content=message,
                llm_provider=model_provider,
                model_name=model_name,
                stream=False,
                memory="Auto",
            )
            print(response.content, flush=True)


def main() -> int:
    try:
        asyncio.run(chat())
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
