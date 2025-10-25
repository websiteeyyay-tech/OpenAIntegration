from datetime import datetime

class ScheduleService:
    def __init__(self):
        self.appointments = []

    def create_appointment(self, client_name, date_str, time_str, property_location):
        try:
            appointment_time = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
            if appointment_time < datetime.now():
                return "❌ Cannot schedule an appointment in the past."

            appointment = {
                "client": client_name,
                "datetime": appointment_time,
                "property": property_location
            }
            self.appointments.append(appointment)
            return f"✅ Appointment booked for {client_name} at {property_location} on {appointment_time.strftime('%b %d, %Y %I:%M %p')}."
        except ValueError:
            return "⚠️ Invalid date or time format. Use YYYY-MM-DD for date and HH:MM (24-hour) for time."

    def list_appointments(self):
        if not self.appointments:
            return "📅 No appointments scheduled."
        lines = ["📋 Upcoming Appointments:"]
        for a in self.appointments:
            lines.append(f"• {a['client']} — {a['property']} on {a['datetime'].strftime('%b %d, %Y %I:%M %p')}")
        return "\n".join(lines)
