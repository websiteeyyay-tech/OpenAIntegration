import json

class DataAnalysis:
    def __init__(self, data_path="data/properties.json"):
        self.data_path = data_path
        self.properties = self.load_data()

    def load_data(self):
        try:
            with open(self.data_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️ File not found: {self.data_path}")
            return []

    def analyze_properties(self):
        if not self.properties:
            return "No property data available."

        total = len(self.properties)
        avg_price = sum(p.get("price", 0) for p in self.properties) / total if total > 0 else 0
        high_value = [p for p in self.properties if p.get("price", 0) > 8000000]

        report = (
            f"📊 Property Data Analysis\n"
            f"Total properties: {total}\n"
            f"Average price: ₱{avg_price:,.2f}\n"
            f"High-value listings (> ₱8M): {len(high_value)}\n"
        )
        return report
