import sys
import os
sys.path.append(os.path.dirname(__file__))

from service.market_forecast import MarketForecast
from service.language_service import LanguageService
from service.ai_service import AIService
from service.ai_intent import AIIntent
from service.schedule_service import ScheduleService
from service.data_analysis import DataAnalysis
from service.automation import Automation
from service.predictive_analysis import PredictiveAnalysis
from service.recommendation_service import RecommendationService
from service.content_service import ContentService
from service.automation_service import AutomationService


def main():
    print("🏠 Real Estate AI Integration System")
    print("Commands:")
    print("  💬 Chat with AI in any language")
    print("  📅 'book appointment', 'show appointments'")
    print("  📊 'analyze data'")
    print("  🤖 'client reply'")
    print("  🧮 'predict trends'")
    print("  🎯 'recommend properties'")
    print("  🖼 'generate description'")
    print("  ⚙️ 'auto follow-up'")
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
    predictor = PredictiveAnalysis("data/market.csv")
    recommender = RecommendationService("data/properties.csv")
    automation_ai = AutomationService()
    automation = Automation("logs/actions.log")
    content_ai = ContentService(api_key)
    forecast = MarketForecast()  # ✅ You forgot to initialize this earlier!

    # Interactive loop
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Detect language
        detected_lang = lang_service.detect_language(user_input)
        translated_input = lang_service.translate(user_input, detected_lang, "en")

        # Detect intent
        intent = intent_ai.detect_intent(translated_input)
        response = ""

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

        elif intent["intent"] == "forecast":
            response = forecast.summarize_market()

        elif intent["intent"] == "analyze_news":
            article = input("Paste real estate news or update: ")
            response = forecast.analyze_news(article)

        elif "predict" in user_input.lower():
            response = predictor.forecast_market_trends()

        elif "recommend" in user_input.lower():
            prefs = {
                "location": input("Preferred location: "),
                "budget": float(input("Budget: ")),
                "bedrooms": int(input("Bedrooms: "))
            }
            response = recommender.recommend(prefs)

        elif "generate description" in user_input.lower():
            data = {
                "location": input("Property location: "),
                "price": input("Price: "),
                "bedrooms": input("Bedrooms: ")
            }
            response = content_ai.generate_description(data)

        elif "auto follow-up" in user_input.lower():
            name = input("Lead name: ")
            response = automation_ai.auto_schedule_followup(name)

        else:
            # Default AI chat fallback
            response = ai.chat(translated_input)

        # Translate AI output back
        translated_output = lang_service.translate(str(response), "en", detected_lang)
        direction = lang_service.get_direction(detected_lang)

        print(f"\n[{detected_lang.upper()} | {direction}] AI: {translated_output}\n")


if __name__ == "__main__":
    main()
