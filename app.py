import json
from google import genai

# Initialize client (uses GEMINI_API_KEY from environment)
client = genai.Client()

def build_prompt(notes: str) -> str:
    return f"""
You are a business writing assistant.

Your task is to:
1. Write a brief meeting summary
2. Provide a clear list of action items

Only include owners and deadlines if they are explicitly mentioned.
Do not make assumptions or invent missing details.

Meeting notes:
{notes}
"""

# Load test cases from external file
with open("eval_set.json", "r", encoding="utf-8") as f:
    test_cases = json.load(f)

# Run all test cases
for item in test_cases:
    case_number = item["case"]
    case_type = item["type"]
    notes = item["input"]

    print(f"\n===== CASE {case_number}: {case_type} =====")

    prompt = build_prompt(notes)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    print("INPUT:")
    print(notes)

    print("\nOUTPUT:")
    print(response.text)
