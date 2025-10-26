import json
import os
from openai import OpenAI

class MarketForecast:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise EnvironmentError("❌ OPENAI_API_KEY not set.")
        self.client = OpenAI(api_key=api_key)

    def summarize_market(self, data_file="data/properties.json"):
        """Generate a natural-language market summary from structured property data."""
        if not os.path.exists(data_file):
            return "❌ Property data file not found."

        with open(data_file, "r") as f:
            data = json.load(f)

        prompt = f"""
        You are an expert real estate analyst. 
        Based on the following property dataset (JSON format), generate a professional, 
        data-driven summary including:
        - Current market trends
        - Pricing patterns
        - Buyer/seller activity
        - Investment opportunities
        - Future forecast (3–6 months)

        Data:
        {json.dumps(data[:10], indent=2)}  # show sample subset
        """

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a professional real estate AI assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7
        )

        return completion.choices[0].message.content.strip()

    def analyze_news(self, news_text: str):
        """Analyze external market news or updates."""
        prompt = f"""
        Analyze this real estate market news and explain its implications for:
        - Property prices
        - Buyer sentiment
        - Developer strategy
        - Investment timing

        News:
        {news_text}
        """

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in real estate market analysis."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.6
        )

        return completion.choices[0].message.content.strip()
