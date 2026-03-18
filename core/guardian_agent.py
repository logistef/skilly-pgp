# core/guardian_agent.py

from typing import List, Dict, Optional
from dataclasses import dataclass

from skilly.core.intent_detector import Skilly, IntentResult


@dataclass
class ToolRoutingResult:
    selected_tool: Optional[str]
    confidence: float
    should_execute: bool
    should_suggest: bool
    reason: str


# Initialize shared Skilly instance
_skilly = Skilly()


def skilly_route_tool(user_input: str, tools: List[Dict]) -> ToolRoutingResult:
    """
    Determine whether a tool should be executed or suggested
    based on Skilly intent detection.

    This represents the "guardian decision layer" in PGP.
    """

    intent_result: IntentResult = _skilly.analyze("user", user_input)

    available_tool_names = {tool["name"] for tool in tools}

    # If detected intent is not available → ignore
    if intent_result.intent not in available_tool_names:
        return ToolRoutingResult(
            selected_tool=None,
            confidence=intent_result.confidence,
            should_execute=False,
            should_suggest=False,
            reason="Intent detected but no matching tool available"
        )

    # Decision thresholds (simple, transparent policy)
    HIGH_CONFIDENCE = 0.85
    MEDIUM_CONFIDENCE = 0.65

    if intent_result.confidence >= HIGH_CONFIDENCE:
        return ToolRoutingResult(
            selected_tool=intent_result.intent,
            confidence=intent_result.confidence,
            should_execute=True,
            should_suggest=False,
            reason="High confidence intent → auto execution"
        )

    if intent_result.confidence >= MEDIUM_CONFIDENCE:
        return ToolRoutingResult(
            selected_tool=intent_result.intent,
            confidence=intent_result.confidence,
            should_execute=False,
            should_suggest=True,
            reason="Medium confidence → suggest action"
        )

    return ToolRoutingResult(
        selected_tool=None,
        confidence=intent_result.confidence,
        should_execute=False,
        should_suggest=False,
        reason="Low confidence → no action"
    )