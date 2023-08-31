import requests

def search_movie_by_title(title, api_key):
    base_url = "http://www.omdbapi.com/"
    params = {
        "apikey": api_key,
        "t": title
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return data

# Substitua "SUA_CHAVE_DE_API" pela sua chave de API real
api_key = "8aa74ee5"
movie_title = "Titanic"  # Substitua pelo título do filme que você deseja pesquisar

movie_data = search_movie_by_title(movie_title, api_key)

if movie_data["Response"] == "True":
    print("Título:", movie_data["Title"])
    print("Ano:", movie_data["Year"])
    print("Gênero:", movie_data["Genre"])
    print("Diretor:", movie_data["Director"])
    print("Atores:", movie_data["Actors"])
    print("IMBD",movie_data["imdbRating"] )
    # Adicione mais informações conforme necessário
else:
    print("Filme não encontrado.")