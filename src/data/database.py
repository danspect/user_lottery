import sqlite3


class Database(object):
    """Classe de banco de dados sqlite3 que armazena dados de uma tabela"""

    def __init__(self):
        """Inicializa as variáveis da classe de banco de dados"""
        # Conecta-se ao banco de dados e cria um cursor
        self.connection = sqlite3.connect("lottery.db")
        self.cursor = self.connection.cursor()

    def close(self):
        """Fecha a conexão com o banco de dados"""
        self.connection.close()

    def execute(self, query):
        """Executa uma consulta SQL no banco de dados"""
        self.cursor.execute(query)

    def commit(self):
        """Salva as alterações no banco de dados"""
        self.connection.commit()

    def create_table(self):
        """Cria uma tabela no banco de dados com os nomes e tipos das colunas especificados"""
        # Cria uma string com a sintaxe SQL para criar a tabela
        sql = '''CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            )'''
        self.execute(sql)

    def insert_user(self, user_name):
        """Insere dados na tabela especificada do banco de dados"""
        # Cria uma string com a sintaxe SQL para inserir os dados
        sql = f'''INSERT INTO Users (name) values ({user_name})'''
        self.execute(sql)

    def get_all_users(self):
        sql = '''SELECT * FROM USERS'''
        self.execute(sql)
