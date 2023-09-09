from ..conexao import conexao

def update_table(tabela, id, nome, email):
    conn, cursor = None, None

    try:
        # Conectando ao banco de dados
        conn, cursor = conexao()

        # Valores para atualizar
        values = (tabela, id, nome, email, id)

        # Executar a consulta SQL
        cursor.execute(f"update MINHA_TABLE set id = {id}, nome = '{nome}', email = '{email}' where id = {id}")

        # Confirmar a transacao
        conn.commit()

        return print('Dados atualizados com sucesso!')

    except(Exception) as e:
        return print('Erro ao realizar atualizacao: ', e)
    
    finally:
        if conn:
            conn.close()
        if cursor:
            cursor.close()

