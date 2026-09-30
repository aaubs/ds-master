# Guide: the ideas you need

A short cheat sheet for the assignment. The session 09 and 10 notebooks explain each idea in more depth.

## The decision

A model gives each student a **risk**: a probability of leaving later this semester. The model does not decide
anything. The study office decides, with a **rule** that turns risks into actions: *contact everyone above a
cut-off*, or *contact the 40 highest risks*. This assignment is about that rule, and the mistakes it makes.

## The four boxes (confusion matrix)

| | not contacted | contacted |
|---|---|---|
| **stayed** | true negative (TN) | **false positive (FP)**: a false alarm |
| **left** | **false negative (FN)**: a missed student | true positive (TP): reached in time |

| Name | Formula | In words |
|---|---|---|
| precision | TP / (TP + FP) | of the students we contacted, the share really at risk |
| recall | TP / (TP + FN) | of the students who left, the share we reached |
| false positive rate | FP / (FP + TN) | of the students who were fine, the share we worried |
| accuracy | (TP + TN) / all | the share handled "correctly". Misleading when few students leave: contacting nobody scores 80 %+ |

A **lower cut-off** contacts more students: recall goes up (fewer missed students), precision goes down (more
false alarms). No cut-off removes both mistakes.

## A cut-off from costs

Contact a student with risk *p* if the expected gain beats the expected cost:

> p × (share a conversation helps) × (cost of a dropout) > (cost of a conversation) + (1 − p) × (cost of a false alarm)

With the notebook's assumptions (helps 30 %, dropout 60,000 DKK, conversation 500 DKK, false alarm 2,000 DKK)
that is p > 12.5 %. The **assumptions are a policy choice**, not a fact: who decides what a false alarm "costs" a
student? This is the same idea as the hotel's cut-off from call costs in session 10.

## Capacity: only 40 conversations

When the office can only hold 40 conversations, the rule becomes "the 40 highest risks", and the cost cut-off only
tells you whether more capacity would pay off. Measure **precision at 40** (how many of the 40 were really at risk)
and **recall at 40** (how many of all who left were among the 40).

## Leakage and time

- Use only what is known at the decision week. A column recorded later (ECTS passed, a deregistration form, the
  *last* login of the semester) makes the model look brilliant and useless.
- Train on earlier cohorts, check on a later one: the model will be used on next year's students.

## Fairness

Compare the four boxes **per group** (here: international and domestic students).
- **Equal recall:** students who would leave are reached equally often in both groups.
- **Calibration within groups:** a risk of 20 % means 20 % in both groups.
When the groups differ, both cannot hold at the same time. Choosing one is a policy decision, and it should be made
and explained by people, not by the model.

## The rules around it

- **EU AI Act:** AI systems used in education to evaluate or steer students are *high-risk*; the obligations
  (human oversight, documentation, transparency, monitoring) apply from 2 December 2027.
- **GDPR:** a score that effectively decides something about a person counts as an automated decision, even if a
  human signs it off. A safe design only *offers help*, is decided by a person, tells students it exists, and lets
  them contest it.

## Storing the model and building the app

- Store the model as the hotel notebook does (section 9): `preprocess.json` + `booster.json`, written and read by the
  hotel app's `portable.py`. Unlike a pickle, these load with any Python version on Streamlit Cloud.
- The hotel app, [aaubs/tonights-front-desk](https://github.com/aaubs/tonights-front-desk), is your template:
  `app.py`, `portable.py`, `requirements.txt` (`streamlit`, `pandas`, `xgboost-cpu`, no version numbers), `model/`.

## Where to read more

- Session 09 lecture notebook: confusion matrix, precision, recall, thresholds.
- Session 10 hotel notebook: the template for every step, especially *Reading the confusion matrix*, *A threshold
  from costs* and *Storing the model properly*.
