import psycopg2
from .config import db_config
from sqlalchemy import create_engine

def conexao_engine():
    try:
        engine = create_engine(f'postgresql://{db_config["PGUSER"]}:{db_config["PGPASSWORD"]}@{db_config["PGHOST"]}:{db_config["PGPORT"]}/{db_config["PGDATABASE"]}')

        return engine
    except Exception as e:
        print('Erro ao conectar no banco de dados: ', e)
