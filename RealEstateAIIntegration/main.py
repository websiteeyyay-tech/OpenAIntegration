import sys
import os
sys.path.append(os.path.dirname(__file__))

from service.language_service import LanguageService
from service.ai_service import AIService
from service.ai_intent import AIIntent
from service.schedule_service import ScheduleService
from service.data_analysis import DataAnalysis
from service.automation import Automation


def main():
    print("🏠 Real Estate AI Integration System")
    print("Commands:")
    print("  💬 Chat with AI in any language")
    print("  📅 'book appointment', 'show appointments'")
    print("  📊 'analyze data'")
    print("  🤖 'client reply'")
    print("  ❌ Type 'exit' to quit\n")

    # Check API Key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Please set your OpenAI API key first:")
        print("export OPENAI_API_KEY=your_api_key_here")
        return

    # Initialize services
    lang_service = LanguageService()
    ai = AIService(api_key)
    intent_ai = AIIntent()
    scheduler = ScheduleService()
    analyzer = DataAnalysis("data/properties.json")
    automation = Automation("logs/actions.log")

    # Interactive loop
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Detect user language
        detected_lang = lang_service.detect_language(user_input)
        translated_input = lang_service.translate(user_input, detected_lang, "en")

        # Determine intent
        intent = intent_ai.detect_intent(translated_input)

        # Handle intent cases
        if intent["intent"] == "schedule":
            client = input("Client name: ")
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM 24hr): ")
            property_loc = input("Property location: ")
            response = scheduler.create_appointment(client, date, time, property_loc)

        elif intent["intent"] == "show":
            response = scheduler.list_appointments()

        elif intent["intent"] == "analyze":
            response = analyzer.analyze_properties()

        elif intent["intent"] == "reply":
            message = input("Client says: ")
            response = automation.reply_to_client(message)

        else:
            # Use AI chat fallback
            ai_response = ai.chat(translated_input)
            response = ai_response

        # Translate AI output back to user’s language
        translated_output = lang_service.translate(response, "en", detected_lang)
        direction = lang_service.get_direction(detected_lang)

        print(f"\n[{detected_lang.upper()} | {direction}] AI: {translated_output}\n")


if __name__ == "__main__":
    main()
