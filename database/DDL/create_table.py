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
        conn.commit()
        
        return print('Tabela criada com sucesso')
    
    except(Exception) as e:
        return print('Erro ao criar a tabela: ', e)
    
    finally:
        if cursor:
            cursor.close()
        if conn:            
            conn.close()
    
scripts = {
    'MINHA_TABLE' : 'CREATE TABLE MINHA_TABLE (ID INT NOT NULL, NOME VARCHAR(20) NOT NULL UNIQUE , EMAIL VARCHAR(50),PRIMARY KEY (ID))',
    'filmes': ''' CREATE TABLE FILMES (
                    title varchar(255),
                    year varchar(255),
                    rated varchar(255),
                    released varchar(255),
                    runtime varchar(255),
                    genre varchar(255),
                    director varchar(255),
                    writer varchar(255),
                    actors varchar(255),
                    plot varchar(255),
                    language varchar(255),
                    country varchar(255),
                    awards varchar(255),
                    poster varchar(255),
                    metascore varchar(255),
                    imdbrating varchar(255),
                    imdbvotes varchar(255),
                    imdbid varchar(255),
                    type varchar(255),
                    dvd varchar(255),
                    boxoffice varchar(255),
                    production varchar(255),
                    website varchar(255),
                    response varchar(255),
                    rating_source_0 varchar(255),
                    rating_value_0 varchar(255),
                    rating_source_1 varchar(255),
                    rating_value_1 varchar(255),
                    rating_source_2 varchar(255),
                    rating_value_2 varchar(255))
    '''
}