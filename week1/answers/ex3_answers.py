"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                                                                                                    
How many guests are you confirming for tonight's event?
Your input ->  160                                                                                                                             
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                                                                                                             

What deposit amount in GBP are you proposing to secure the booking?
Your input ->                                                                                                                                  
2026-04-11 19:42:29 INFO     rasa.dialogue_understanding.generator.command_generator  - [info     ] Invalid message                errors=[{'error_type': 'rasa_internal_error_user_input_empty', 'info': {}, 'command': 'error'}] event_key=command_generator.evaluate_message.error
I see an empty message. What can I assist you with?
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                                                                                                    
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->  no
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Is there anything else I can help you with?
Your input ->  yes, calling to confirm a booking                                                                                               
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                                                      
And how many of those guests will need vegan meals?
Your input ->  50                                                                                                                              
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  600                                                                                                                             
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £600 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "The issue is: a deposit of £600 exceeds the organiser's authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Is there anything else I can help you with?
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?                                                                                       
I am afraid, I don't know the answer. At this point, I don't have access to a knowledge base.
Would you like to resume confirm booking and handle out of scope?
Your input ->  handle out of scope                                                                                                             
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
It said that it doesn't know how to handle the request and
suggest to return to the path that it knows how to handle.
Though after I decided to continue with the happy path, it
skipped the vegan number question and conformed the booking with
the default 0 vegan meals, without asking about it again.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
RASA CALM's handling due to its interactive nature was able to suggest
an alternative path that it can handle, while LangGraph just said
that it can't handle the request.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
Uncommented to]he new condition.
Ran a conversation with valid booking details and confirmed the agent escalated
immediately with the 16:45 deadline message instead of confirming the booking.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
Firstly I don't understand why we need to compare the current CALM version
with something old, no longer used, which we never used or planned to use.

The LLM now handles less structured responses — parsing "about 160 people" → 160.0 — which
required Python regex before. Python still enforces business rules (deposit cap,
capacity limit) because those checks must be deterministic; an LLM might rationalise
exceptions. The gain is less boilerplate code. The cost is that LLM routing is
probabilistic and harder to audit than the explicit rules.yml paths it replaced.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
The setup cost bought a multi-turn, step-by-step interaction with the user —
CALM collects one slot at a time, can ask for clarification, and has a defined
fallback to suggest to the user. LangGraph runs a single prompt and executes tools
independently without user interaction. CALM also enforces a fixed
step order and only uses tools declared in flows.yml; the LLM only parses
user input, not decides what to do next. For a booking confirmation that
helps to gather several all the information reliably.
"""
