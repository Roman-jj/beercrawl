import json
import pandas as pd
import analyse  # Ensure analyse.py is in the same directory or installed as a module


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

# Filter unique beers by Untappd beer ID
df = df.drop_duplicates(subset=["bid"], keep="first")

# 1. Define date range
start = pd.Timestamp("2023-09-06")   # Sep 2023
end   = pd.Timestamp("2025-05-24")   # May 2025
# 2. Filter by date range
filtered = df[(df["created_at"] >= start) & (df["created_at"] <= end)]


# print(filtered[["beer_name", "created_at"]].tail())
print(filtered.shape[0])

analyse.country_checkin_count(df)

analyse.beer_style_count(df)
analyse.beer_style_avg_rating(df)
analyse.country_avg_rating(df)