import sqlite3 as sq

# Conecta ao banco de dados e cria o cursor
con = sq.connect('agenda.db')
cursor = con.cursor()

# Comando para inserir dados nas tabelas individualmente
cursor.execute("""
    insert into clientes(nome, cpf)
    values ("Jean Charles", "000.000.000-00")
""")
# Adicionar vários dados de uma vez
cadastros = [
    # Lebrando que também podem ser variaveis incluidas através do input na lista
    ("Junior Paiva", "111.111.111-11"),
    ("Jose Lucas", "222.222.222-22"),
    ("Leandro", "333.333.333-33")
]

cursor.executemany("""
    insert into clientes (nome, cpf)
    values(?,?)
""", cadastros) # Aqui é colocado a lista que oculpara as interrogações



# Salva os dados no banco de dados e fecha a conexão
con.commit()
con.close()
