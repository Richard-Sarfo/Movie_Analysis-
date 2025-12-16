import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_revenue_vs_budget(df: pd.DataFrame):
    plt.figure(figsize=(8, 4))
    plt.scatter(
        df['budget_musd'],
        df['revenue_musd'],
        alpha=0.5,
        color='blue',
        label='Movies'
    )
    plt.xlabel('Budget (Million USD)')
    plt.ylabel('Revenue (Million USD)')
    plt.title('Revenue vs Budget')
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_roi_by_genre(df: pd.DataFrame):
    plt.figure(figsize=(10, 5))
    sns.boxplot(
        x='genres',
        y='roi',
        data=df,
        palette='Set2'
    )
    plt.title("ROI Distribution by Genre")
    plt.xlabel("Genre")
    plt.ylabel("ROI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_popularity_vs_rating(df: pd.DataFrame):
    plt.figure(figsize=(8, 4))
    plt.scatter(
        df['popularity'],
        df['vote_average'],
        alpha=0.6,
        color='green',
        label='Movies'
    )
    plt.xlabel('Popularity')
    plt.ylabel('Rating')
    plt.title('Popularity vs Rating')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_yearly_trends(df: pd.DataFrame):
    df['release_year'] = df['release_date'].dt.year
    yearly = df.groupby('release_year').agg(
        mean_revenue=('revenue_musd', 'mean'),
        mean_budget=('budget_musd', 'mean')
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        yearly.index,
        yearly['mean_revenue'],
        label='Mean Revenue',
        color='orange',
        marker='o'
    )
    plt.plot(
        yearly.index,
        yearly['mean_budget'],
        label='Mean Budget',
        color='blue',
        marker='o'
    )
    plt.xlabel('Year')
    plt.ylabel('Million USD')
    plt.title('Yearly Average Revenue & Budget')
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_franchise_vs_standalone_revenue(franchise_movies, standalone_movies):
    franchise_mean_rev = franchise_movies['revenue_musd'].mean()
    standalone_mean_rev = standalone_movies['revenue_musd'].mean()

    plt.figure(figsize=(6, 4))
    plt.bar(
        ['Franchise', 'Standalone'],
        [franchise_mean_rev, standalone_mean_rev],
        color=['orange', 'blue'],    
    )
    plt.ylabel('Million USD')
    plt.title('Franchise vs Standalone: Mean Revenue')
    plt.tight_layout()
    plt.show()
