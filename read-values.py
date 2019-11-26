import sqlite3 as sq
con = sq.connect('agenda.db')
cursor = con.cursor()

cursor.execute("""
    select * from clientes
""")

for linha in cursor.fetchall():
    print(linha)

con.close()