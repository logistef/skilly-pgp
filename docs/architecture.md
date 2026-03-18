# Skilly Architecture — Parallel Guardian Pattern (PGP)

This document describes the architectural design of Skilly as a reference implementation of the **Parallel Guardian Pattern (PGP)**.

The focus is on **clear separation of responsibilities**, low-latency execution, and reliable action detection in AI systems.

---

## 🧠 Architectural Principle

Skilly is built around a simple idea:

> Separate **reasoning** from **action decision-making**

Instead of relying on a single model to perform both tasks,  
the system introduces a **parallel deterministic layer** that evaluates intent independently.

---

## 🏗 High-Level Architecture

```text
User Input
├──→ LLM (Creative Layer)
└──→ Skilly Guardian (Deterministic Layer)

            ↓
     Orchestrator Layer
            ↓
     Tool / Skill Execution
            ↓
     Result Integration
            ↓
        Final Response
🔧 Core Components
1. Creative Layer (LLM)

Responsibilities:

Natural language understanding

Context interpretation

Response generation

Characteristics:

Probabilistic

Flexible

Capable of reasoning and abstraction

The LLM is not responsible for reliable action detection.

2. Guardian Layer (Skilly)

Responsibilities:

Detect actionable intent

Assign confidence scores

Suggest or trigger tool execution

Implementation:

Embedding-based similarity matching

Predefined intent space

Deterministic scoring

Characteristics:

Fast (milliseconds)

Stable across repeated inputs

Independent of LLM variability

3. Orchestrator Layer

The orchestrator combines outputs from both layers.

Responsibilities:

Merge LLM response and guardian signal

Apply execution policies

Decide between:

no action

suggestion

automatic execution

Example policy:

if confidence > 0.85:
    auto-execute
elif confidence > 0.65:
    suggest action
else:
    ignore
4. Tool / Skill Layer

Executes the actual operations.

Examples:

filesystem operations

web search

system commands

device control

Requirements:

idempotent where possible

observable (logs, outputs)

secure and scoped

5. Result Integration Layer

After execution:

Tool output is captured

Fed back into the LLM

Used to generate a final, grounded response

🔁 Execution Flow (Step-by-Step)

User sends input

LLM begins generating a response

Guardian analyzes input in parallel

Guardian outputs:

intent

confidence

actionable flag

Orchestrator evaluates policy

If triggered:

tool executes

result captured

LLM integrates result into final answer

⚡ Parallelism Model

Key design choice:

The guardian does not wait for the LLM.

Both operate simultaneously:

LLM → handles conversation

Guardian → evaluates action

This ensures:

no added latency

faster overall response

immediate intervention when needed

🧩 Data Flow Overview
User Input
   ↓
[ LLM ] --------→ Draft Response
   ↓
[ Guardian ] → Intent + Confidence
   ↓
[ Orchestrator ]
   ↓
[ Tool Execution ] (optional)
   ↓
[ Result Injection ]
   ↓
Final LLM Output
🔒 Design Considerations
Determinism vs Flexibility

LLM → flexible, creative

Guardian → deterministic, stable

The system intentionally separates these qualities.

Safety & Control

Sensitive actions can be:

gated by confidence thresholds

restricted by policy

logged for auditing

Extensibility

The architecture supports:

multiple guardians (domain-specific)

multiple tool layers

pluggable LLM backends

Backend Independence

Skilly does not depend on a specific model.

Compatible with:

local inference (llama.cpp, GGUF)

cloud APIs

hybrid deployments

🧬 Scaling the Pattern

The Parallel Guardian Pattern can evolve into:

multi-guardian systems (per domain)

hierarchical orchestration layers

policy-driven execution engines

This allows gradual transition from:

simple assistants

to full AI-driven automation systems

🧠 Key Takeaway

This architecture is not about replacing the LLM.

It is about:

Structuring intelligence so that each component does one thing reliably

LLM → think

Guardian → detect intent

Orchestrator → decide

Tools → act

🔚 Summary

Skilly demonstrates how a small architectural addition can:

improve reliability

reduce ambiguity in action detection

enable scalable AI system design

The Parallel Guardian Pattern is designed to be:

simple to integrate

low overhead

high impact