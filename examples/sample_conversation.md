# Sample Conversation — Parallel Guardian Pattern (PGP)

This example demonstrates how Skilly operates alongside an LLM  
to detect actionable intent and improve system reliability.

---

## 🧩 Scenario: Filesystem Inspection

### User Input

```
Can you check what’s inside /var/log?
```

---

## 🧠 Parallel Processing

### 1. LLM (Creative Layer)

The LLM interprets the request conversationally:

```
Sure, the /var/log directory typically contains system logs such as authentication logs, kernel logs, and service logs.
```

---

### 2. Skilly (Guardian Layer)

At the same time, Skilly evaluates the input:

```json
{
  "intent": "filesystem.list",
  "confidence": 0.91,
  "actionable": true
}
```

---

## ⚙️ Orchestrator Decision

Based on confidence thresholds:

- Confidence > 0.85 → Auto-execute

Decision:

```python
filesystem.list("/var/log")
```

---

## 🔧 Tool Execution

```
/var/log/
├── syslog
├── auth.log
├── kern.log
├── dpkg.log
```

---

## 🔁 Result Integration

The tool result is injected back into the LLM.

---

## 💬 Final Response

```
Here’s what I found in /var/log:

- syslog
- auth.log
- kern.log
- dpkg.log

These logs typically contain system-level events, authentication records and kernel activity. Let me know if you want me to inspect any specific file.
```

---

## 🧠 What Happened Here

- The LLM provided context and explanation  
- Skilly detected actionable intent with high confidence  
- The system executed the correct tool automatically  
- The final response was grounded in real data  

---

## ⚡ Key Benefit

Without the guardian layer:

- The LLM might only explain what `/var/log` is  
- The action could be missed entirely  

With Skilly:

- Action is reliably detected  
- Execution is immediate  
- Output is accurate and useful  

---

## 🧩 Scenario: Medium Confidence (Suggestion)

### User Input

```
Maybe you can take a look at my files?
```

---

### Skilly Output

```json
{
  "intent": "filesystem.list",
  "confidence": 0.68,
  "actionable": true
}
```

---

### Orchestrator Decision

- Confidence between 0.65 and 0.85 → Suggest

---

### System Response

```
I can help with that. Would you like me to list the files in a specific folder?
```

---

## 🧠 What Happened Here

- Intent detected, but not strongly enough  
- System avoids incorrect execution  
- User remains in control  

---

## 🚫 Scenario: Low Confidence (No Action)

### User Input

```
My system feels weird today
```

---

### Skilly Output

```json
{
  "intent": null,
  "confidence": 0.32,
  "actionable": false
}
```

---

### System Behavior

- No action triggered  
- LLM handles response normally  

---

### LLM Response

```
That could be caused by several things. Do you notice any specific issues like slow performance or errors?
```

---

## 🔚 Summary

This example highlights the core strength of the Parallel Guardian Pattern:

- High confidence → automatic execution  
- Medium confidence → suggestion  
- Low confidence → no intervention  

The result is a system that is:

- responsive  
- reliable  
- controlled  

---

## 💡 Key Insight

The LLM does not need to be perfect at deciding actions.

It only needs to be good at conversation.

