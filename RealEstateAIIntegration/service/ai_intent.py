from openai import OpenAI
import re
from datetime import datetime, timedelta


class AIIntent:
    def __init__(self):
        self.client = OpenAI()

    def detect_intent(self, message: str):
        """
        Uses AI to detect what the user wants (schedule, show, analyze, reply, etc.).
        Returns a dict: {"intent": "schedule", "data": {...}}
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an intent detection AI for a real estate assistant. "
                        "You convert user messages into structured commands."
                    )
                },
                {
                    "role": "user",
                    "content": f"User said: '{message}'. Return JSON with an 'intent' key like schedule/show/analyze/reply/forecast/etc."
                }
            ]
        )

        content = response.choices[0].message.content.strip().lower()

        # Simple keyword-based fallback for robustness
        if "schedule" in message.lower() or "appointment" in message.lower() or "book" in message.lower():
            return {"intent": "schedule"}

        elif "show" in message.lower() or "list" in message.lower() or "appointments" in message.lower():
            return {"intent": "show"}

        elif "analyze" in message.lower() or "analysis" in message.lower():
            return {"intent": "analyze"}

        elif "reply" in message.lower() or "respond" in message.lower() or "client" in message.lower():
            return {"intent": "reply"}

        elif "forecast" in message.lower() or "future" in message.lower() or "market" in message.lower():
            return {"intent": "forecast"}

        elif "news" in message.lower() or "update" in message.lower() or "trend" in message.lower():
            return {"intent": "analyze_news"}

        elif "predict" in message.lower():
            return {"intent": "predict"}

        elif "recommend" in message.lower() or "suggest" in message.lower():
            return {"intent": "recommend"}

        elif "generate description" in message.lower() or "property description" in message.lower():
            return {"intent": "generate_description"}

        elif "auto follow-up" in message.lower() or "follow up" in message.lower():
            return {"intent": "auto_followup"}

        else:
            return {"intent": "unknown"}
