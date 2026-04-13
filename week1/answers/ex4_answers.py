"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "2 Hunter Square, Edinburgh"
# Had to modify a prompt to get query 2 to work properly with this model.
QUERY_2_FINAL_ANSWER  = "No matches found."
# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = "It was just mcp_venue_server.py file that needed changes. Not much to say here but need 30 words, MCP server tools are in one place in the server code and that is updated."

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 200   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 100   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP allows to discover the existing tools on demand. Tools are no longer
tied to the agent code, can be modified and deployed separately.
Also MCP server tools can be used by multiple different agents without
modifications needed.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- Planner: upstream reasoning model that breaks the raw task into subgoals before
  the ReAct loop starts — lives in the autonomous-loop half.
- Executor: research_agent.py from Week 1, the fast inner-loop worker that calls
  tools and iterates inside the autonomous half.
- Shared MCP tool server: both halves discover tools from it dynamically, so
  neither is coupled to specific tool implementations.
- Handoff bridge: routes control between the loop and the structured agent when
  one half needs what the other does — research vs. human conversation.
- Rasa CALM structured agent: handles the auditable, high-stakes conversational
  tasks (deposit calls, confirmations) in the structured-agent half.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph for research, Rasa for the call. In the Exercise 2 runs, the ReAct loop
naturally pivoted when Bow Bar was full and chained tools in whatever order made
sense — that flexibility is the point. Rasa did the opposite: fixed flow, explicit
escalation rule when the deposit was too high, no improvisation. Swapping feels
wrong because Rasa can't reason across unknown tool outputs, and the ReAct loop has no business-rule guardrails
(it could plausibly confirm a deposit it shouldn't). Each one breaks badly in the
other's role.
"""