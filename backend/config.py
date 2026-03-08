import os
from dotenv import load_dotenv
load_dotenv()
PASSWORD = os.getenv('DB_PASSWORD')
""" CONFIGURAÇÕES DO BANCO DE DADOS """
DB_HOST = 'localhost'
DB_USER = 'root'
DB_NAME = 'barbearia_db'

""" CONFIGURAÇÕES DO FLASK """
DEBUG = True
PORT = 5000
