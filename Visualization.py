import matplotlib.pyplot as plt
import pandas as pd

# Revenue vs Budget Trends
def plot_revenue_vs_budget(df: pd.DataFrame):
    plt.figure(figsize=(8, 4))
    plt.scatter(df['budget_musd'], df['revenue_musd'], alpha=0.5)
    plt.xlabel('Budget (Million USD)')
    plt.ylabel('Revenue (Million USD)')
    plt.title('Revenue vs Budget')
    plt.tight_layout()
    plt.show()


# ROI Distribution by Genre
def plot_roi_by_genre(df: pd.DataFrame):
    df.boxplot(column='roi', by='genres', rot=45, grid=True,figsize=(8, 4))
    plt.title("ROI Distribution by Genre")
    plt.suptitle("")  
    plt.xlabel("Genre")
    plt.ylabel("ROI")
    plt.xticks(rotation=45)
    plt.show()

# Popularity vs Rating
def plot_popularity_vs_rating(df: pd.DataFrame):
    plt.figure()
    plt.scatter(df['popularity'], df['vote_average'])
    plt.xlabel('Popularity')
    plt.ylabel('Rating')
    plt.title('Popularity vs Rating')
    plt.tight_layout()
    plt.show()


# Yearly Trends in Box Office Performance
def plot_yearly_trends(df: pd.DataFrame):
    yearly = df.groupby('release_year').agg(
        mean_revenue=('revenue_musd', 'mean'),
        mean_budget=('budget_musd', 'mean')
    )

    # Yearly Average Revenue
    plt.figure()
    plt.plot(yearly.index, yearly['mean_revenue'])
    plt.xlabel('Year')
    plt.ylabel('Mean Revenue (M USD)')
    plt.title('Yearly Average Revenue')
    plt.tight_layout()
    plt.show()

    # Yearly Average Budget
    plt.figure()
    plt.plot(yearly.index, yearly['mean_budget'])
    plt.xlabel('Year')
    plt.ylabel('Mean Budget (M USD)')
    plt.title('Yearly Average Budget')
    plt.tight_layout()
    plt.show()


# Franchise vs Standalone Revenue
def plot_franchise_vs_standalone_revenue(franchise_movies: pd.DataFrame, standalone_movies: pd.DataFrame):
    franchise_mean_rev = franchise_movies['revenue_musd'].mean()
    standalone_mean_rev = standalone_movies['revenue_musd'].mean()

    plt.figure()
    plt.bar(['Franchise', 'Standalone'], [franchise_mean_rev, standalone_mean_rev], color=['Orange', 'Blue'])
    plt.ylabel('Mean Revenue (M USD)')
    plt.title('Franchise vs Standalone: Mean Revenue')
    plt.tight_layout()
    plt.show()
