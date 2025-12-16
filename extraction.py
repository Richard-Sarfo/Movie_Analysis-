import requests

#Function for extrating the movie data
def movie(movie_id, key):
    url = url = f"https://api.themoviedb.org/3/movie/{movie_id}?append_to_response=credits&api_key={key}"


    #try and except blocks to handle errors 
    try:
        response = requests.get(url,timeout=5)
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Movie ID {movie_id} not found (404). Skipping.")
        elif response.status_code == 401:
            print("Invalid API key (401). Check your KEY.")
        else:
            print(f"HTTP error occurred for Movie ID {movie_id}: {http_err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Request error for Movie ID {movie_id}: {err}")
        return None

    return response.json()
