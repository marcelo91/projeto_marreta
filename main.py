import requests
import json
import config
import api_filmes

def carrega_filmes():
    # Carregando os filmes da API do site omdbapi.com
    lista_filmes_api = []

    # ler arquivo com a lista de titulos de filmes    
    with open('data/amostra_filmes.txt', 'r') as arquivo_filmes:
        filmes = arquivo_filmes.readlines()
        arquivo_filmes.close()

    # Buscar os filmes da API
    for filme in filmes:
        filme = filme.strip()

        lista_filmes_api.append(api_filmes.get_movie_info(filme, config.api_config['api_key']))

    return lista_filmes_api

def salva_arquivo():
    # Salvar a lista de filmes da API em arquivo JSON

    # Recebe lista e arquivos
    lista_filmes_api = carrega_filmes()

    # Arquivo para salvar os dados
    with open('data/movie_data.json', 'w') as json_file:
        for filme in lista_filmes_api:
            json.dump(filme, json_file)
            json_file.write('\n')
    
    print('Arquivo gerado com sucesso!')

def trata_json():
    # Tratar o conteúdo do retorno da API

    # Recebe lista e arquivos
    lista_filmes_api = carrega_filmes()

    # Verificando se a TAG Ratings possui valor ou objeto e realizando o devido tratamento
    for filme_api in lista_filmes_api:
        i = 0
        if isinstance(filme_api['Ratings'], list):
            # Passados os objetos
            for df_ratings in filme_api['Ratings']:
                # continuar