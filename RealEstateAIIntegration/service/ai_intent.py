from openai import OpenAI
import re
from datetime import datetime, timedelta

class AIIntent:
    def __init__(self):
        self.client = OpenAI()

    def detect_intent(self, message: str):
        """
        Uses AI to detect what the user wants (schedule, show, analyze, or reply).
        Returns a dict: {"intent": "schedule", "data": {...}}
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an intent detection AI for a real estate assistant. You convert user messages into structured commands."},
                {"role": "user", "content": f"User said: '{message}'. Return JSON with intent (schedule/show/analyze/reply/unknown) and details like client name, date, time, property."}
            ]
        )

        content = response.choices[0].message.content.strip()

        # Very simple fallback
        if "schedule" in message.lower():
            return {"intent": "schedule"}
        elif "analyze" in message.lower():
            return {"intent": "analyze"}
        elif "appointment" in message.lower() or "show" in message.lower():
            return {"intent": "show"}
        elif "reply" in message.lower() or "client" in message.lower():
            return {"intent": "reply"}
        else:
            return {"intent": "unknown"}

        # Optionally: parse JSON from model if you want deep details
