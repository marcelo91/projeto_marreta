from ..conexao import conexao

def consulta(table):
    conn, cursor = None, None

    try:
        # Conectando ao banco de dados
        conn, cursor = conexao()

        # Comando SQL para criar uma tabela
        query = f'select * from {table}'
        
        # Executando o comando SQL
        cursor.execute(query)

        # Exibindo retorno do select
        print(cursor.fetchall())

    except(Exception) as e :
        print(f'Erro ao consultar a tabela: {table}, erro: {e}')

    finally:
        # Certifique-se de fechar o cursor e a conexão, independentemente de sucesso ou falha.
        if conn:
            conn.close()
    if cursor:
        cursor.close()