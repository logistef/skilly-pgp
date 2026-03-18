# Skilly-pgp  
### A Parallel Guardian Pattern for Reliable AI Systems

> A deterministic oversight layer for LLM-based systems — improving intent detection, tool execution, and overall reliability.

---

![status](https://img.shields.io/badge/status-experimental-blue)
![pattern](https://img.shields.io/badge/architecture-Parallel%20Guardian%20Pattern-purple)
![focus](https://img.shields.io/badge/focus-reliability%20over%20guessing-orange)

---

⚠️ This repository is a **conceptual reference implementation**.  
The focus is on architecture and pattern design, not production completeness.

---

*A lightweight cognitive architecture for reliable, tool-aware AI systems.*

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
```

---

## 🔗 Embedding Models

Skilly relies on embedding-based semantic matching.  
Any modern embedding model can be used.

**Examples:**

- BAAI/bge-small-en-v1.5 (default in this repo)  
- sentence-transformers/all-MiniLM-L6-v2  

The architecture is model-agnostic — the key value lies in how embeddings are used, not which model is selected.

---

### 2. Basic Intent Detection

```python
from skilly.core.intent_detector import Skilly

skilly = Skilly()

result = skilly.analyze("user", "List files in my documents folder")

print(result.intent)        # filesystem.list
print(result.confidence)    # 0.87
print(result.actionable)    # True
```

---

### 3. Tool Routing Example

```python
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
```

---

### 4. Parallel Guardian Pattern (Minimal)

```python
from skilly.core.intent_detector import Skilly

skilly = Skilly()

def process(user_input):
    llm_response = f"LLM: {user_input}"

    intent = skilly.analyze("user", user_input)

    if intent.actionable and intent.confidence > 0.8:
        return {
            "llm": llm_response,
            "guardian": f"Detected {intent.intent}"
        }

    return {"llm": llm_response}

print(process("List files in /var/log"))
```

---

## 🌟 Why This Pattern Matters

Mainstream LLM systems still treat tool use as a sequential pipeline:

```
User → LLM → function_call → tool → LLM → user
```

This approach often struggles with:

- missed tool intents  
- inconsistent function calls  
- hallucinated actions  
- high latency  
- heavy reliance on a single model’s reasoning  

The Parallel Guardian Pattern (PGP) corrects these weaknesses by introducing  
a second evaluation layer that operates independently of the LLM’s reasoning.

---

## 🧠 The Parallel Guardian Pattern (PGP)

PGP introduces two complementary cognitive tracks:

### 1. Creative Track (LLM)

Handles:
- language  
- reasoning  
- conversation  

### 2. Guardian Track (Skilly)

An embedding-based intent engine that:

- detects tool-relevant semantics  
- operates deterministically  
- reacts in milliseconds  
- intervenes when needed  

> A creative AI supported by a deterministic semantic watchdog.

---

## 🔥 Why Embeddings?

Embeddings are:

- deterministic  
- stable  
- fast  
- robust  

This makes them ideal for:

- file operations  
- system actions  
- search  
- structured tasks  

LLMs imagine.  
Embeddings provide signal.

---

## 🔧 How Skilly Works (Flow)

```
User Message
├──→ LLM (response)
└──→ Skilly (intent detection)

        if high-confidence
                ↓
        action triggered
```

---

## ⚡ Advantages of PGP

- ✔ Instant responses  
- ✔ Reduced hallucination risk  
- ✔ Transparent control  
- ✔ Backend-agnostic  
- ✔ Lower latency  

---

## 🧩 Example

**User:**  
“Can you check the log files in folder X?”

**LLM:**  
“Sure, those logs often contain valuable information.”

**Skilly:**  
“High-confidence filesystem intent detected.”

**Result:**  
Tool executes → result returned → LLM finalizes response

---

## 🏗 Architecture Overview

```
        ┌─────────────────────────────┐
        │             User             │
        └─────────────┬───────────────┘
                      │
    ┌─────────────────┴─────────────────┐
    │                                   │
┌───────▼────────┐        ┌──────────▼─────────┐
│ Creative LLM   │        │ Skilly Guardian     │
└───────┬────────┘        └──────────┬──────────┘
        │                             │
        └───────────────┬─────────────┘
                        │
              ┌─────────▼─────────┐
              │ Tool Layer        │
              └─────────┬─────────┘
                        │
              ┌─────────▼─────────┐
              │ Final Output       │
              └────────────────────┘
```

---

## 🧬 Core Ideas

- Parallel > sequential  
- Reliability must be designed  
- Embeddings provide stability  
- LLMs are not execution engines  
- Separation of concerns  

---

## 🌐 Part of a Larger Vision

Skilly fits into a broader modular AI ecosystem where agents, tools, and reasoning  
layers are composed into reliable systems.

---

## 🚧 Proof-of-Concept

A full implementation will be published soon.

---

## 💬 Why I’m Building This

If you're working on complex systems and enjoy improving how they behave under real conditions, feel free to reach out.

— Stephan Badert
