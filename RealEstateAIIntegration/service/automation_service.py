import datetime
import os

class AutomationService:
    def __init__(self, log_path="logs/automation.log"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    def auto_schedule_followup(self, lead_name):
        """
        Automatically schedule a follow-up reminder for leads.
        """
        next_date = datetime.date.today() + datetime.timedelta(days=2)
        message = f"📅 Follow-up scheduled with {lead_name} on {next_date}."
        self._log_action(f"Follow-up created for {lead_name} on {next_date}")
        return message

    def track_task_completion(self, task):
        """
        Log when a task is completed automatically.
        """
        now = datetime.datetime.now()
        self._log_action(f"✅ Task completed: {task} at {now}")
        return f"Task '{task}' marked as completed at {now.strftime('%H:%M %p')}."

    def risk_flag(self, description):
        """
        Flag potential compliance or risk issues in property transactions.
        """
        flagged = any(word in description.lower() for word in ["unauthorized", "pending", "violation"])
        if flagged:
            self._log_action(f"🚨 Risk detected: {description}")
            return "⚠️ Risk flagged for compliance review."
        return "✅ No risks detected."

    def _log_action(self, text):
        with open(self.log_path, "a") as f:
            f.write(f"{datetime.datetime.now()} - {text}\n")
