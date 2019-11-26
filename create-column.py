import sqlite3 as sq
con = sq.connect('agenda.db')
cursor = con.cursor()

cursor.execute("""
    alter table clientes
    add column boolean
""")
con.commit()
con.close()