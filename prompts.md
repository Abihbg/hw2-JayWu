# Prompt Iteration

## Initial Version

You are a business writing assistant.

Your task is to:
1. Write a brief meeting summary
2. Provide a clear list of action items


### Observed Issues

The initial prompt performs well on structured inputs (Cases 1 and 2), producing clear summaries and action items.

However, several problems appear in less structured cases:
- The model invents tasks, owners, and deadlines that are not explicitly stated (Case 3).
- It introduces implicit next steps even when none are mentioned (Case 4).
- It fails to acknowledge uncertainty and instead generates plausible but unsupported outputs (Case 5).

These behaviors indicate that the model prioritizes producing complete and structured outputs over staying faithful to the input.


---

## Revision 1

You are a business writing assistant.

Your task is to:
1. Write a brief meeting summary
2. Provide a clear list of action items

Only include owners and deadlines if they are explicitly mentioned.
Do not invent missing details or make assumptions.


### Changes and Reasoning

Revision 1 was designed to address the hallucination problem observed in the initial version.

Specifically:
- The instruction “Do not invent missing details” was added to discourage the model from generating unsupported content.
- The constraint on owners and deadlines was introduced to prevent the model from filling in missing structure.

This change directly responds to Cases 3 and 4, where the model added fabricated tasks and responsibilities.


### Observed Impact

- Performance on structured inputs (Cases 1 and 2) remained unchanged.
- There was a slight reduction in overconfident phrasing.
- However, the model still generated inferred tasks and responsibilities in ambiguous inputs (Case 3).
- The model continued to introduce implicit next steps in cases where none were explicitly stated (Case 4).

Overall, Revision 1 improved instructions but did not fundamentally change the model’s tendency to “complete” missing information.


---

## Revision 2

You are a business writing assistant.

Your task is to:
1. Write a brief meeting summary
2. Provide a clear list of action items

Only include owners and deadlines if they are explicitly mentioned.
Do not invent missing details or make assumptions.

If the information is unclear, incomplete, or conflicting, explicitly say "Needs human review".


### Changes and Reasoning

Revision 2 was introduced because Revision 1 did not sufficiently control hallucination.

The key insight from Revision 1 was:
- The model still prefers generating structured outputs rather than admitting uncertainty.

Therefore, Revision 2 adds an explicit fallback behavior:
- When information is unclear, the model should stop generating content and instead signal uncertainty using “Needs human review”.

This change specifically targets Case 5, where the input contains conflicting and incomplete information.


### Observed Impact

- Performance on structured inputs (Cases 1 and 2) remained stable.
- However, the model still failed to consistently follow the “Needs human review” instruction.
- In ambiguous cases (Cases 3 and 5), the model continued to generate assumed tasks and placeholders such as “[Assign Name]”.
- The model still prioritized producing complete outputs over strictly following constraints.

Overall, Revision 2 clarified expected behavior but did not fully override the model’s tendency to infer and generate missing details.
