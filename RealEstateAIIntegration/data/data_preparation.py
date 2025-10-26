import pandas as pd
import json
import os

# Paths
raw_properties = "data/properties_ph.csv"
raw_market = "data/market_trends_ph.csv"
clean_dir = "data/cleaned"

os.makedirs(clean_dir, exist_ok=True)

def clean_property_data():
    print("🧹 Cleaning property dataset...")
    df = pd.read_csv(raw_properties)

    # Normalize column names
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Drop empty rows
    df.dropna(subset=["price", "location"], inplace=True)

    # Convert price to numeric (remove ₱, commas)
    df["price"] = (
        df["price"]
        .astype(str)
        .replace({"₱": "", ",": ""}, regex=True)
        .astype(float)
    )

    # Basic filtering
    df = df[df["price"] > 100000]  # remove invalid rows

    df.to_json(f"{clean_dir}/properties_clean.json", orient="records", indent=2)
    print("✅ Cleaned property data saved.")


def clean_market_data():
    print("📈 Cleaning market trend dataset...")
    df = pd.read_csv(raw_market)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.dropna(inplace=True)

    df["date"] = pd.to_datetime(df["date"])
    df.sort_values("date", inplace=True)

    summary = {
        "latest_value": df["value"].iloc[-1],
        "quarter": str(df["date"].iloc[-1].date()),
        "trend": "rising" if df["value"].iloc[-1] > df["value"].iloc[-2] else "falling",
    }

    with open(f"{clean_dir}/trends_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("✅ Cleaned market trend data saved.")


if __name__ == "__main__":
    clean_property_data()
    clean_market_data()
    print("🎯 Data preparation complete.")
