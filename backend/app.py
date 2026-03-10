from flask import Flask, send_from_directory  # IMPORTA O FLASK PARA CRIAR O SERVIDOR
from models import Database  # IMPORTA A CLASSE DATABASE DO MODELS.PY
import os

frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')

app = Flask(__name__) # CRIA O SERVIDOR FLASK


db = Database() # CRIA UMA INSTÂNCIA DO BANCO DE DADOS

@app.before_request # ANTES DE CADA REQUISIÇÃO, CONECTA AO BANCO
def conectar_banco():
    db.conectar()

@app.route('/')
def servir_frontend():
    return send_from_directory(frontend_dir, 'index.html')

@app.route('/<path:filename>')
def servir_arquivos(filename):
    return send_from_directory(frontend_dir, filename)

if __name__ == '__main__': # "estou sendo executado diretamente?"
    app.run()  # Flask, começa a escutar requisições!