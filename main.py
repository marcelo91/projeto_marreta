import requests
import pandas as pd
import json
import config
import api_filmes
from database.conexao_engine import conexao_engine

def carrega_filmes():
    # Carregando os filmes da API do site omdbapi.com
    lista_filmes_api = []

    # ler arquivo com a lista de titulos de filmes    
    with open('data/filmes.txt', 'r') as arquivo_filmes:
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
    df_consolida = []
    # Tratar o conteúdo do retorno da API

    # Recebe lista e arquivos
    lista_filmes_api = carrega_filmes()

    # Verificando se a TAG Ratings possui valor ou objeto e realizando o devido tratamento
    for filme_api in lista_filmes_api:
        i = 0
        df_ratings = []

        if isinstance(filme_api['Ratings'], list):
            # Passados os objetos
            for df_ratings in filme_api['Ratings']:
                tag_source = 'Rating_Source_' + str(i)
                tag_value = 'Rating_Value_' + str(i)
                filme_api[tag_source] = df_ratings["Source"]
                filme_api[tag_value] = df_ratings["Value"]
                i += 1
        else:
            filme_api['Rating_Source_0'] = filme_api['Source']
            filme_api['Rating_Value_0'] = filme_api['Value']

        filme_api.pop('Ratings')
        df_consolida.append(filme_api)
    
    pd.set_option('display.max_columns', None)
    df_filme = pd.DataFrame(df_consolida)
    df_filme.columns = df_filme.columns.str.lower()

    return df_filme

def inseri_filmes():
    
    # Recebi o DataFrame filme
    df_filme = trata_json()

    # Conexao com Banco de Dados
    engine = conexao_engine()

    # Insert, 'append' = adiciona, 'replace' = apaga dos dados da tabela e coloca os dados do datafram, 'fail' = erro se a tabela estiver criada
    df_filme.to_sql('filmes', engine, if_exists='replace', index=False)

inseri_filmes()