import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

def country_avg_rating(df):
    """
    Plot average rating by brewery country.
    
    Args:
        df (pd.DataFrame): cleaned dataframe with at least columns:
            - 'brewery_country'
            - 'rating_score'
    """
    # --- Average rating per country ---
    countries = df["brewery_country"].value_counts().head(25)
    df = df[df["brewery_country"].isin(countries.index)]
    avg_rating = df.groupby("brewery_country")["rating_score"].mean().sort_values(ascending=False)

    plt.figure(figsize=(10,6))
    avg_rating.plot(kind="bar")
    plt.title("Countries (Top 25) by Average Rating")
    plt.xlabel("Country")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    #plt.savefig("avg_rating_by_country.png", dpi=300)
    #plt.close()

def beer_style_avg_rating(df):
    # --- Average rating per beer style ---
    styles = df["beer_type"].value_counts().head(25)
    df = df[df["beer_type"].isin(styles.index)]
    avg_style_rating = df.groupby("beer_type")["rating_score"].mean().sort_values(ascending=False)
    
    plt.figure(figsize=(10,6))
    avg_style_rating.plot(kind="bar")
    plt.title("Beer Styles (Top 25) by Average Rating")
    plt.xlabel("Beer Style")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    #plt.savefig("top_beer_styles_by_avg_rating.png", dpi=300)
    #plt.close()

def country_checkin_count(df):
    # --- Number of checkins per country ---
    checkins = df["brewery_country"].value_counts()
    # print(checkins)
    # print(checkins.sum())

    plt.figure(figsize=(10,6))
    checkins.plot(kind="bar")
    plt.title("Number of Check-ins per Country")
    plt.ylabel("Check-ins")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    #plt.savefig("checkins_per_country.png", dpi=300)
    #plt.close()

def beer_style_count(df):
    # --- Number of beers per style ---
    styles = df["beer_type"].value_counts()
    print(styles)

    plt.figure(figsize=(10,6))
    styles.head(20).plot(kind="bar")
    plt.title("Top 20 Beer Styles")
    plt.ylabel("Number of Beers")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
    #plt.savefig("top_beer_styles.png", dpi=300)
    #plt.close()

def example_analysis(df):
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