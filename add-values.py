import sqlite3 as sq

# Conecta ao banco de dados e cria o cursor
con = sq.connect('agenda.db')
cursor = con.cursor()

# Comando para inserir dados nas tabelas
cursor.execute("""
    insert into clientes(nome, cpf)
    values ("Jean Charles", "616.803.353-08")
""")

cursor.execute("""
    insert into clientes(nome, cpf)
    values ("Francisco Amoedo", "000.000.000-00")
""")

# Salva os dados no banco de dados e fecha a conexão
con.commit()
con.close()
