import sqlite3 as sq

# Comando para conectar com o arquivo .db que já deve estar criado
con = sq.connect('agenda.db')

# Cursor é o agente iterador que permite a manipulação de dados em um database
cursor = con.cursor()

# Comando qu cria as tabelas, dentro usamos sintaxe SQL normalmente
cursor.execute("""
    CREATE TABLE clientes(
        id integer primary key autoincrement not null,
        nome text not null,
        cpf  text not null
    );
""")

# Fecha a conexão com o banco de dados
con.close()