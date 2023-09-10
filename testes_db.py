from database.conexao import conexao
from database.DDL.create_table import cria_tabela
from database.DML.select import consulta
from database.DML.insert import insert_table
from database.DML.delete import delete_table
from database.DML.update import update_table


# cria_tabela('MINHA_TABLE')
# consulta('MINHA_TABLE')

# insert_table('MINHA_TABLE', 1, 'Felipe', 'felipe@email.com')
# consulta('MINHA_TABLE')

# update_table('MINHA_TABLE', 1, 'Felipe', 'felipe@hotmail.com')
# consulta('MINHA_TABLE')

# delete_table('MINHA_TABLE', 1)
# consulta('MINHA_TABLE')

consulta('filmes')