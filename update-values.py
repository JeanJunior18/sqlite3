import sqlite3 as sq
con = sq.connect('agenda.db')
cursor = con.cursor()

updid = 1
newName = "Gustavo Falcão"
newCPF = "999.999.999-99"

# Configura as atualizações e seleciona o id do valor a ser alterado
cursor.execute("""
    update clientes 
    set nome = ?, cpf = ?
    where id = ?
""",(newName,newCPF,updid))

con.commit()
con.close()