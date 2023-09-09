import psycopg2
from .config import db_config

# print(db_config['PGHOST'])

def conexao():
    conn = psycopg2.connect (
        host = db_config['PGHOST'],
        port = db_config['PGPORT'],
        user = db_config['PGUSER'],
        password = db_config['PGPASSWORD'],
        database = db_config['PGDATABASE']
        )
    return conn, conn.cursor()
