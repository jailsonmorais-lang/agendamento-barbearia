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