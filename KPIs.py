#Function for streamline ranking 
def rank_movies(df, column, ascending=False, n=10, min_budget=None, min_votes=None):
    temp = df.copy()

    if min_budget:
        temp = temp[temp['budget_musd'] >= min_budget]

    if min_votes:
        temp = temp[temp['vote_count'] >= min_votes]

    return temp.sort_values(by=column, ascending=ascending).head(n)

