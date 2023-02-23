import requests
import json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMDNiZjg2YWFmNDZlMTkwZWJjNGYwMjI2ZTlkZmIyNCIsInN1YiI6IjYzZjNkMDI1ZTk0MmVlMDBkYjJhNjQwZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KGM5Sc88atqmYAUOaVFEWz3ZK2vSqGwOnxT7qR1Q3tM"

def get_popular_movies(list_type):
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = 'https://image.tmdb.org/t/p/'
    return f'{base_url}{size}/{poster_api_path}'


def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()