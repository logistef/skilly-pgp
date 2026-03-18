# Skilly — A Parallel Guardian Pattern for Improving LLM Systems  
*A new cognitive architecture for tool-aware, reliable AI pipelines.*

Skilly is the reference implementation of the **Parallel Guardian Pattern (PGP)**,  
a design approach that lets a deterministic, embedding-based guardian agent  
run *in parallel* with a Large Language Model (LLM) to improve intent detection,  
tool-calling accuracy and overall system robustness.

Instead of relying on the LLM alone to decide when actions should be taken,  
Skilly provides a **stable oversight layer** that nudges  
the AI when a user request clearly implies a tool or skill execution.

---

## 🚀 Getting Started

This is a minimal example showing how Skilly detects intent and supports action routing.

### 1. Install

```bash
pip install sentence-transformers numpy scikit-learn torch
2. Basic Intent Detection
from skilly.core.intent_detector import Skilly

skilly = Skilly()

result = skilly.analyze("user", "List files in my documents folder")

print(result.intent)        # filesystem.list
print(result.confidence)    # 0.87
print(result.actionable)    # True
3. Tool Routing Example
from skilly.core.guardian_agent import skilly_route_tool

tools = [
    {"name": "filesystem.list"},
    {"name": "search.web"}
]

routing = skilly_route_tool(
    "Search for AI trends",
    tools
)

print(routing)
4. Parallel Guardian Pattern (Minimal)
from skilly.core.intent_detector import Skilly

skilly = Skilly()

def process(user_input):
    # Simulated LLM response
    llm_response = f"LLM: {user_input}"

    # Skilly runs in parallel
    intent = skilly.analyze("user", user_input)

    if intent.actionable and intent.confidence > 0.8:
        return {
            "llm": llm_response,
            "guardian": f"Detected {intent.intent}"
        }

    return {"llm": llm_response}

print(process("List files in /var/log"))
🌟 Why This Pattern Matters

Mainstream LLM systems still treat tool use as a sequential pipeline:

User → LLM → function_call → tool → LLM → user

This approach often struggles with:

missed tool intents

inconsistent function calls

hallucinated actions

high latency

heavy reliance on a single model’s reasoning

The Parallel Guardian Pattern (PGP) corrects these weaknesses by
introducing a second evaluation layer that operates independently
of the LLM’s creative reasoning.

🧠 The Parallel Guardian Pattern (PGP)

PGP introduces two separate, complementary cognitive tracks:

1. Creative Track (LLM)

Handles natural language, nuance, reasoning, conversation, narrative.

2. Guardian Track (Skilly)

An embedding-based intent engine that:

detects tool-relevant semantics

operates deterministically

reacts in milliseconds

intervenes when the LLM misses an action

Together:

A creative AI supported by a deterministic semantic watchdog
that only steps in when action is actually required.

🔥 Why Embeddings?

Embeddings are:

deterministic

stable

geometric

extremely fast

robust even in long conversations

This makes them well-suited for detecting:

file operations

system interactions

searches

device actions

structured tasks

LLMs can imagine.
Embeddings provide stable signal.
PGP leverages that difference.

🔧 How Skilly Works (Flow)
User Message
├──→ LLM: generates a natural-language reply
└──→ Skilly: embedding-based intent detection

        if high-confidence tool-intent
                    ↓
     Skilly suggests or triggers action

The orchestrator then:

executes the appropriate skill

returns the result

feeds it back into the LLM

All without delaying the initial answer.

⚡ Advantages of PGP
✔ Instant responses

While the LLM talks, Skilly evaluates in parallel.

✔ Reduced hallucination risk in action detection

Because action detection is separated from generative reasoning.

✔ Transparent oversight

User sees when Skilly intervenes and why.

✔ Backend-agnostic

Works with local LLMs, cloud models, llama.cpp, Mistral, OpenAI, Anthropic…

✔ Natural self-improvement

Tool outcomes feed back into the intent engine.

🧩 Example

User:
“Can you check the log files in folder X?”

LLM:
“Sure, those logs often contain valuable information.”

Skilly:
“High-confidence filesystem intent detected.
Would you like me to list the files in folder X?”

Result:
Tool executes → result returns → LLM finalizes with real data.

🏗 Architecture Overview
        ┌─────────────────────────────┐
        │             User             │
        └─────────────┬───────────────┘
                      │
    ┌─────────────────┴─────────────────┐
    │                                   │
┌───────▼────────┐        ┌──────────▼─────────┐
│ Creative LLM   │        │ Skilly Guardian     │
│ (Parallel Eval)│        │ (Embedding Intent)  │
└───────┬────────┘        └──────────┬──────────┘
        │                             │
        │ Natural Reply               │ Intervention
        └───────────────┬─────────────┘
                        │
              ┌─────────▼─────────┐
              │ Tool / Skill Layer │
              └─────────┬─────────┘
                        │
                  Tool Results
                        │
              ┌─────────▼─────────┐
              │ Final LLM Output   │
              └────────────────────┘
🧬 Core Ideas

Parallel evaluation > sequential pipelines

Reliability must be designed, not assumed

Embeddings provide stable intent detection

LLMs excel at reasoning, not execution decisions

Systems benefit from layered responsibility

🌐 Part of a Larger Vision

Skilly and the Parallel Guardian Pattern (PGP) are components of a broader
modular ecosystem focused on building flexible, low-latency, reliable AI orchestration.
This approach integrates naturally into systems such as AI_MASTERMIND, where agents, tools,
and cognition layers work together in a composable architecture.

🚧 Proof-of-Concept

A full proof-of-concept implementing Skilly and the Parallel Guardian Pattern
is underway and will be published here soon.

💬 Footnote — Why I am Building This

If you're part of an innovative tech environment with likeminded people
who enjoy analysing, challenging and improving complex systems, feel free to reach out.

— Stephan Badert, creator of the Parallel Guardian Pattern (PGP).
