from ..conexao import conexao

def insert_table(tabela, id, nome, email):
    conn, cursor = None, None

    try:
        # Conectando ao banco de dados
        conn, cursor = conexao()

        # Valores para inserir
        values = (id, nome, email)

        # Executar a consulta SQL
        cursor.execute(script[tabela], values)

        # Confirmar a transacao
        conn.commit()

        return print('Dados inseridos com sucesso!')

    except(Exception) as e:
        return print('Erro ao realizar insert: ', e)
    
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()

script = {
    'MINHA_TABLE': 'INSERT INTO MINHA_TABLE (ID, NOME, EMAIL) VALUES (%s, %s, %s)'
}