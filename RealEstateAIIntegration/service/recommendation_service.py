import pandas as pd

class RecommendationService:
    def __init__(self, data_path="data/properties.csv"):
        self.data_path = data_path

    def recommend(self, preferences):
        """
        Recommend properties based on user preferences.
        """
        try:
            df = pd.read_csv(self.data_path)

            # Filter based on preferences
            filtered = df[
                (df["location"].str.contains(preferences["location"], case=False, na=False)) &
                (df["price"] <= preferences["budget"]) &
                (df["bedrooms"] == preferences["bedrooms"])
            ]

            if filtered.empty:
                return f"⚠️ No properties match your preferences in {preferences['location']}."

            results = "\n🏘 Recommended Properties:\n"
            for _, row in filtered.iterrows():
                results += f"• {row['name']} - {row['location']} (₱{row['price']:,}) | {row['bedrooms']} BR\n"

            return results

        except FileNotFoundError:
            return "⚠️ Property data file not found. Please ensure 'data/properties.csv' exists."
        except Exception as e:
            return f"❌ Error loading property recommendations: {str(e)}"
