import requests
import json

# Função para fazer a requisição ao OMDB
def get_movie_info(movie_name, api_key):
    base_url = "http://www.omdbapi.com/"
    params = {
        't': movie_name,
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Sua chave de API do OMDB
api_key = '8aa74ee5'

# Abrir e ler o arquivo de texto
with open('data/filmes.txt', 'r') as file:
    movie_names = file.readlines()

# Iterar sobre os nomes de filme e fazer requisições
with open('data/movie_data.json', 'w') as json_file:
    for movie_name in movie_names:
        movie_name = movie_name.strip()
        movie_data = get_movie_info(movie_name, api_key)
        
        if movie_data['Response'] == 'True':
            json.dump(movie_data, json_file)
            json_file.write('\n')  # Adicionar uma quebra de linha após cada objeto JSON
        else:
            print(f"Erro ao obter informações para o filme: {movie_name}")

print("Dados salvos no arquivo 'movie_data.json'.")
