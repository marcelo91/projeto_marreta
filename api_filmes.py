import requests

# Função para fazer a requisição ao OMDB
def get_movie_info(movie_name, api_key):
    base_url = "http://www.omdbapi.com/"
    params = {
        't': movie_name,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()