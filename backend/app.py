from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
from models import Database  # Adicionado o import necessário
from routes import routes_bp # Importe o seu Blueprint

app = Flask(__name__)
CORS(app) 

# Registra as rotas da API
app.register_blueprint(routes_bp) 

db = Database()

# Definindo o caminho do frontend
frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.before_request
def conectar_banco():
    db.conectar()

@app.route('/')
def servir_frontend():
    return send_from_directory(frontend_dir, 'index.html')

@app.route('/<path:arquivo>')
def servir_arquivos(arquivo):
    endereco_do_arquivo = os.path.join(frontend_dir, arquivo)
    if os.path.exists(endereco_do_arquivo) and not os.path.isdir(endereco_do_arquivo):
        return send_from_directory(frontend_dir, arquivo)
    
    return jsonify({'erro': 'Recurso não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)