import json
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

def clean_numeric_columns(df, numeric_cols):
    """
    Convert selected columns in a DataFrame to numeric (floats).
    Invalid values are coerced to NaN and can optionally be dropped later.
    
    Args:
        df (pd.DataFrame): Your dataframe
        numeric_cols (list): Column names to convert
    
    Returns:
        pd.DataFrame: DataFrame with cleaned numeric columns
    """
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

# --- Load JSON file ---
with open("untappd_export_25-09-25.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)
numeric_fields = ["rating_score", "beer_abv", "beer_ibu", 
                  "global_rating_score", "global_weighted_rating_score"]
df = clean_numeric_columns(df, numeric_fields)
df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

# --- Example filtering ---
# Keep only beers with rating >= 4
filtered = df[df["rating_score"] >= 4]

# --- Example aggregation ---
# Average rating per beer type
avg_ratings = filtered.groupby("beer_type")["rating_score"].mean().sort_values(ascending=False)

# --- Plotting ---
plt.figure(figsize=(10,6))
avg_ratings.plot(kind="bar")
plt.title("Average Ratings of Beers (rating >= 4)")
plt.xlabel("Beer Type")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Count check-ins per month
checkins_per_month = df.groupby(df["created_at"].dt.to_period("M")).size()

checkins_per_month.plot(kind="bar", figsize=(10,5))
plt.title("Check-ins per Month")
plt.xlabel("Month")
plt.ylabel("Number of Check-ins")
plt.tight_layout()
plt.show()