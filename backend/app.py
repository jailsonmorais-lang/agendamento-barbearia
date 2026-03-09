from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db
import os

# CONFIGURAÇÃO DE PASTAS (O segredo para o Railway não dar 404)
# Isso garante que o Flask ache a pasta 'frontend' não importa onde ele seja executado
base_dir = os.path.abspath(os.path.dirname(__file__))
frontend_dir = os.path.join(base_dir, '..', 'frontend')

app = Flask(__name__)
CORS(app)

@app.before_request
def conectar_banco():
    db.conectar()

# IMPORTAR ROUTES (Mantendo sua lógica original)
from routes import *

# ROTA RAIZ: É aqui que o Railway faz o "Health Check"
@app.route('/')
def servir_frontend():
    # Isso envia o seu index.html quando alguém acessa o site
    return send_from_directory(frontend_dir, 'index.html')

# ROTA PARA CSS, JS E ÍCONES:
@app.route('/<path:filename>')
def servir_arquivos(filename):
    # Se o navegador pedir 'style.css' ou 'script.js', ele busca na pasta frontend
    return send_from_directory(frontend_dir, filename)

# ROTA ESPECÍFICA PARA A PASTA ICONES (Caso o navegador peça /Icones/...)
@app.route('/Icones/<path:filename>')
def servir_icones(filename):
    icones_dir = os.path.join(frontend_dir, 'Icones')
    return send_from_directory(icones_dir, filename)

if __name__ == '__main__':
    # O Railway passa a porta automaticamente pela variável de ambiente PORT
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
