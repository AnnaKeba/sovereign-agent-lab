"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
All formats let to the correct answers. I tried adding more distractions and
other modifications, but the example seems too siimple even for the small
old models to fail on them.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Albanach"
PART_B_XML_ANSWER      = "The Haymarket Vaults"
PART_B_SANDWICH_ANSWER = "The Haymarket Vaults"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
I did not manage to get the model distracted by the existing or added disctractors,
the idea of the task is clear and I felt like I don't need to spend time further trying
to come up with the representative failing example.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Similarly to part B, even the smallest model got the correct answer in all formats. 
The idea of the task is clear, but it's too simple to show the desired behavior. I felt like I don't need to spend time further trying
to come up with the representative failing example, since the idea is clear.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
The idea of the task was to show how the inportant information in the middle can 
get forgotten or lost, especially when there is distracting information in the
context. However this example was way too simple to represent this behavior, and 
even the smallest model got the correct answer in all formats. I felt like I don't need to spend time further trying
to come up with the representative failing example, since the idea is clear.
"""