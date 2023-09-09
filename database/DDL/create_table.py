from ..conexao import conexao

def cria_tabela(tabela):
    conn, cursor = None, None

    try:
        # Conectando ao banco de dados
        conn, cursor = conexao()

        # Comando SQL para criar uma tabela
        query = scripts[tabela]
        
        # Executando o comando SQL
        cursor.execute(query)

        # Commit da transação (salva as alterações)        
        return print('Tabela criada com sucesso')
    
    except(Exception) as e:
        return print('Erro ao criar a tabela: ', e)
    
    finally:
        if cursor:
            cursor.close()
        if conn:            
            conn.close()
    
scripts = {
    'MINHA_TABLE' : 'CREATE TABLE MINHA_TABLE (ID INT NOT NULL, NOME VARCHAR(20) NOT NULL UNIQUE , EMAIL VARCHAR(50),PRIMARY KEY (ID))'
}