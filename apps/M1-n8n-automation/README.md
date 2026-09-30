# n8n templates · session 11 (automation)

Two workflows to import into n8n and change into your own. The full guide (set-up, free LLM keys, ideas,
troubleshooting) is on Moodle.

| File | What it does | Needs |
|---|---|---|
| `1-ask-the-model-shelf.json` | A form for a hotel booking → the model on the [model shelf](https://models.automate.business.aau.dk) → the probability of a cancellation on the form's final page | nothing |
| `2-ask-the-model-shelf-gemini.json` | The same, and Gemini writes a confirmation email to the guest when the risk is high | a Google Gemini credential (free key from [aistudio.google.com](https://aistudio.google.com)) |

**Import:** in n8n, *Workflows → Create → ⋯ → Import from file*, or copy the whole JSON and paste it onto an empty
canvas. **Run:** *Execute workflow* opens the form.

**Use your own model:** put it on the shelf with the
[packaging notebook](https://colab.research.google.com/github/aaubs/ds-master/blob/main/notebooks/M1_11_model_shelf.ipynb),
then change the URL in *Ask the model shelf* to `https://models.automate.business.aau.dk/m/<your-model>/predict` and
the form fields to your model's columns (the model's documentation page lists them).
