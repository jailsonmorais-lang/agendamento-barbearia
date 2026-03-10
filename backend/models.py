import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE, DB_PORT

class Database:
    def __init__(self):
        self.connection = None

    def conectar(self):
        self.connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE,
            port=DB_PORT
            )
        
    def obter_dados(self, query, valores=None):
        escreva = self.connection.cursor(dictionary=True)
        escreva.execute(query, valores)
        return escreva.fetchall()
    
    def executar_query(self, query, valores=None):
        escreva = self.connection.cursor()
        escreva.execute(query, valores)
        self.connection.commit()
        return True