from flask import Flask, send_from_directory
from flask_cors import CORS
from models import db
import os


app = Flask(__name__)
CORS(app)

@app.before_request
def conectar_banco():
    db.conectar()

# IMPORTAR ROUTES (que tem as rotas)
from routes import *

@app.route('/')
def servir_frontend():
    frontend_dir = os.path.join(app.root_path, '..', 'frontend')
    return send_from_directory(frontend_dir, 'index.html')

@app.route('/static/<path:filename>')
def servir_arquivos(filename):
    frontend_dir = os.path.join(app.root_path, '..', 'frontend')
    return send_from_directory(frontend_dir, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
