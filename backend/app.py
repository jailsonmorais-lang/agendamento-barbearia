from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db
import os

# Ajuste de caminhos: base_dir é a pasta 'backend'
base_dir = os.path.dirname(os.path.abspath(__file__))
# frontend_dir sobe um nível e entra na pasta 'frontend'
frontend_dir = os.path.abspath(os.path.join(base_dir, '..', 'frontend'))

app = Flask(__name__)
CORS(app)

@app.before_request
def conectar_banco():
    db.conectar()

# Importa as rotas do seu arquivo routes.py
from routes import *

# Rota principal para o index.html (O que o Railway testa)
@app.route('/')
def servir_frontend():
    return send_from_directory(frontend_dir, 'index.html')

# Rota para carregar style.css, script.js e imagens
@app.route('/<path:filename>')
def servir_arquivos(filename):
    return send_from_directory(frontend_dir, filename)

# ROTA ESPECÍFICA PARA A PASTA ICONES (Caso o navegador peça /Icones/...)
@app.route('/Icones/<path:filename>')
def servir_icones(filename):
    icones_dir = os.path.join(frontend_dir, 'Icones')
    return send_from_directory(icones_dir, filename)

if __name__ == '__main__':
    # O Railway define a porta automaticamente
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
