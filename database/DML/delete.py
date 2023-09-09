from ..conexao import conexao

def delete_table(tabela, id):
    conn, cursor = None, None

    try:
        # Conectando ao banco de dados
        conn, cursor = conexao()

        # Executar a consulta SQL
        cursor.execute(f'delete from {tabela} where id = {id}')

        # Confirmar a transacao
        conn.commit()

        return print('Dados dletetados com sucesso!')

    except(Exception) as e:
        return print('Erro ao realizar delete: ', e)
    
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()
