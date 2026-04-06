import json
from pathlib import Path
from google import genai

# Configurable settings
MODEL_NAME = "gemini-2.5-flash"
INPUT_FILE = "eval_set.json"
OUTPUT_FILE = "output.txt"

# Initial prompt version
SYSTEM_PROMPT = """
You are a business writing assistant.

Your task is to:
1. Write a brief meeting summary
2. Provide a clear list of action items
""".strip()


def build_prompt(notes: str) -> str:
    return f"{SYSTEM_PROMPT}\n\nMeeting notes:\n{notes}"


def load_test_cases(file_path: str) -> list[dict]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("eval_set.json must contain a list of test cases.")

    return data


def run_case(client: genai.Client, case: dict) -> str:
    case_number = case.get("case", "Unknown")
    case_type = case.get("type", "Unknown Type")
    notes = case.get("input", "").strip()

    if not notes:
        return (
            f"===== CASE {case_number}: {case_type} =====\n"
            f"INPUT:\n[Empty input]\n\n"
            f"OUTPUT:\nNo input was provided for this case.\n"
        )

    prompt = build_prompt(notes)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    output_text = response.text if response.text else "[No response text returned]"

    return (
        f"===== CASE {case_number}: {case_type} =====\n"
        f"INPUT:\n{notes}\n\n"
        f"OUTPUT:\n{output_text}\n"
    )


def main() -> None:
    client = genai.Client()
    test_cases = load_test_cases(INPUT_FILE)

    all_results = []

    for case in test_cases:
        result = run_case(client, case)
        print(result)
        print("-" * 60)
        all_results.append(result)

    Path(OUTPUT_FILE).write_text(
        "\n" + ("-" * 60 + "\n").join(all_results),
        encoding="utf-8"
    )

    print(f"\nAll outputs were saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
