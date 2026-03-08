import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT


class Database:
    def __init__(self):
        self.connection = None

    def conectar(self):
        """ CONECTA AO BANCO DE DADOS MySQL """
        try:
            self.connection = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                port=DB_PORT,
                ssl_disabled=False
            )
            print('✅ Conectado ao banco de dados!')
            return True
        except mysql.connector.Error as erro:
            print(f'❌ Erro ao conectar: {erro}')
            return False

    def desconectar(self):
        """ DESCONECTA DO BANCO DE DADOS """
        if self.connection:
            self.connection.close()
            print('✅ Desconectado do banco de dados!')

    def executar_query(self, query, dados=None):
        """ EXECUTA UMA QUERY NO BANCO """
        try:
            cursor = self.connection.cursor()
            if dados:
                cursor.execute(query, dados)
            else:
                cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.Error as erro:
            print(f'❌ Erro na query: {erro}')
            return False

    def obter_dados(self, query, valores=None):
        """ OBTÉM DADOS DO BANCO """
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, valores)
            return cursor.fetchall()
        except mysql.connector.Error as erro:
            print(f'❌ Erro ao obter dados: {erro}')
            return False


""" CRIAR INSTÂNCIA DO BANCO """
db = Database()
