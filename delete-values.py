import sqlite3 as sq
con = sq.connect('agenda.db')
cursor = con.cursor()

delId = 6

# Seleciona a tabela e o id que vai ser deletado
cursor.execute("""
    delete from clientes
    where id = ?
""",(delId,))

con.commit()
con.close()