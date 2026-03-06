from flask import Flask
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)

@app.before_request
def conectar_banco():
    db.conectar()

# IMPORTAR ROUTES (que tem as rotas)
from routes import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)