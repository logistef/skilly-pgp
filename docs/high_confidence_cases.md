# High Confidence Intent Cases

This document outlines examples of user inputs where the Skilly guardian
can detect actionable intent with **high confidence** using embedding-based matching.

These cases represent scenarios where the Parallel Guardian Pattern (PGP)
provides immediate value by enabling reliable and deterministic action detection.

---

## 🧠 What Defines a High-Confidence Case

A high-confidence case typically has:

- Clear intent  
- Low ambiguity  
- Direct mapping to a known action  
- Minimal dependency on conversational nuance  

These are ideal for deterministic detection.

---

## 📁 1. Filesystem Operations

### Example Inputs

- "List files in my documents folder"
- "Show me what’s inside /var/log"
- "Open the downloads directory"
- "Delete the file report.pdf"

### Detected Intent

```text
filesystem.list
filesystem.open
filesystem.delete
Why High Confidence

Strong keyword signals ("list", "open", "delete")

Clear object (file, folder, path)

Low ambiguity in user intention

🌐 2. Web Search & Information Retrieval
Example Inputs

"Search for AI trends in 2025"

"Look up the latest news about NVIDIA"

"Find documentation for FastAPI"

Detected Intent
search.web
search.documentation
Why High Confidence

Explicit verbs ("search", "find", "look up")

Clear expectation of external data retrieval

No dependency on conversational interpretation

⚙️ 3. System Commands
Example Inputs

"Check CPU usage"

"Show running processes"

"Restart the server"

"Get disk space usage"

Detected Intent
system.monitor
system.process.list
system.restart
Why High Confidence

Standardized terminology

Strong mapping to system-level actions

Common across environments

📡 4. Device & IoT Actions
Example Inputs

"Turn off the lights"

"Set temperature to 22 degrees"

"Start the robot vacuum"

"Lock the front door"

Detected Intent
device.control.light.off
device.control.thermostat.set
device.control.vacuum.start
device.control.lock
Why High Confidence

Clear command structure

Known device/action combinations

Minimal ambiguity

📦 5. Application-Level Actions
Example Inputs

"Create a new project"

"Deploy the application"

"Run the tests"

"Build the Docker image"

Detected Intent
app.project.create
app.deploy
app.test.run
app.build.docker
Why High Confidence

Common developer workflows

Recognizable action verbs

Structured intent patterns

⚠️ Boundary Cases (Lower Confidence)

Not all inputs are suitable for deterministic detection.

Example Inputs

"Can you maybe take a look at my files?"

"I wonder what’s going on with my system"

"It feels slow today"

Why Lower Confidence

Ambiguous intent

Lack of explicit action verbs

Requires interpretation and context

👉 These cases remain the responsibility of the LLM.

🧩 Key Insight

High-confidence cases are not about complexity.

They are about:

clarity of intent + stability of language patterns

This is where embedding-based detection excels.

🔁 Role in the Parallel Guardian Pattern

In these scenarios:

Skilly detects intent instantly

High confidence triggers:

automatic execution

or direct suggestion

The LLM:

provides explanation

contextualizes results

maintains conversational flow

🔚 Summary

High-confidence intent detection enables:

reliable automation

predictable system behavior

reduced dependency on LLM interpretation

These cases form the foundation for building
robust, production-ready AI systems using the Parallel Guardian Pattern.