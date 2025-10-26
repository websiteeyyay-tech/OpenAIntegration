import pandas as pd
from datetime import datetime
import random

class PredictiveAnalysis:
    def __init__(self, data_path="data/market.csv"):
        self.data_path = data_path

    def forecast_market_trends(self):
        """
        Simulates property market trend forecasting.
        """
        try:
            df = pd.read_csv(self.data_path)
            avg_growth = df["price_growth"].mean()
            forecast_year = datetime.now().year + 1
            forecast = avg_growth * random.uniform(0.9, 1.2)

            return (
                f"📈 Based on market data, the projected property price growth "
                f"for {forecast_year} is approximately {forecast:.2f}%.\n"
                "Factors: location demand, interest rates, and investment activity."
            )

        except FileNotFoundError:
            return "⚠️ Market data file not found. Please ensure 'data/market.csv' exists."
        except Exception as e:
            return f"❌ Error analyzing market data: {str(e)}"
