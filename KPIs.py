#Function for streamline ranking 
def rank_movies(df, column, ascending=False, n=None, min_budget=None, min_votes=None):
    """
    Rank and filter movies by a specified column.
    
    Args:
        df: DataFrame with movie data
        column: Column name to sort by
        ascending: Sort order (default: False for descending)
        n: Number of top results to return (default: None for all)
        min_budget: Minimum budget in millions USD (default: None)
        min_votes: Minimum vote count threshold (default: None)
    
    Returns:
        Filtered and sorted DataFrame with top N movies
    """
     
    temp = df.copy()

    if min_budget:
        temp = temp[temp['budget_musd'] >= min_budget]

    if min_votes:
        temp = temp[temp['vote_count'] >= min_votes]

    return temp.sort_values(by=column, ascending=ascending).head(n)

