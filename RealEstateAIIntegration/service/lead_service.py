class LeadService:
    def __init__(self):
        self.leads = []

    def qualify_lead(self, message):
        # very simple scoring logic
        score = 0
        if "buy" in message.lower(): score += 2
        if "budget" in message.lower(): score += 2
        if "location" in message.lower(): score += 1
        return "High" if score >= 4 else "Medium" if score >= 2 else "Low"

    def save_lead(self, name, contact, interest):
        self.leads.append({"name": name, "contact": contact, "interest": interest})
        return f"✅ Lead saved: {name} ({interest})"
