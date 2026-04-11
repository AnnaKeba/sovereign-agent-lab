"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = [
    "check_pub_availability",
    "calculate_catering_cost",
    "get_edinburgh_weather",
    "generate_event_flyer",
]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = False

TASK_A_NOTES = """The prompt in task A didn't actually request to confirm a single venue,
so the agent expectedly returned both correct options - Albanach and Haymarket Vaults.
The `generate_event_flyer` function is only asked to be implemented in Task B.
That's why I am posting results of task A before `generate_event_flyer` is implemented and returns stub and error.
Final output of the model: `Both venues met all constraints (capacity + vegan). The Haymarket Vaults (capacity 160) exactly met the minimum; The Albanach (capacity 180) had headroom. generate_event_flyer was called for both venues but returned stub errors.`
After I implemented the function and everything became successful, the agent started choosing
one venue as a preference, but again the prompt is not precise enough and doesn't enforce this.
"""
# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-d9cba3e1-6935-4e47-8c15-de97f3478bcc_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
With the given prompt, the agent pivoted to checking other venues after confirming that 
The Bow Bar was unavailable immediately started checking other venues. But the prompt was not precise
enough, so the agent kept checking avaliable venues until it ran out of turns. I slightly fixed
the prompt, now it does the same, but returns the first available venue without looping.
"""

SCENARIO_1_FALLBACK_VENUE = "FILL_ME_IN"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = "Unfortunately, none of the known venues meet the capacity and dietary requirements. The Albanach, The Haymarket Vaults, and The Guilford Arms have a capacity of 180, 160, and 200 respectively, which is less than the required capacity of 300. The Bow Bar has a capacity of 80, which is also less than the required capacity, and it is currently full. Therefore, it is not possible to find a venue from the known venues that meets the requirements."

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "Your input is lacking necessary details. Please provide more information or specify the task you need help with."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
It depends on the level of risk the user is willing to take. If the user
wants to be careful and make sure to only use tested tools, then this behaviour could be acceptable.
However, if the user is open to the agent trying to find a solution, the agent should be able to try
to find options to solve it (browsing, etc) and again, depending on the risk level, either come back
to the user with the proposal and request to try it out, or try out independantly if the user
is open to high risk independent actions.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
PASTE MERMAID OUTPUT HERE
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
FILL ME IN
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
FILL ME IN
"""
