import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMDNiZjg2YWFmNDZlMTkwZWJjNGYwMjI2ZTlkZmIyNCIsInN1YiI6IjYzZjNkMDI1ZTk0MmVlMDBkYjJhNjQwZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KGM5Sc88atqmYAUOaVFEWz3ZK2vSqGwOnxT7qR1Q3tM"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"