from flask import Blueprint, request, jsonify
from models import Database 
import bcrypt

# Criamos o Blueprint em vez de usar @app.route
routes_bp = Blueprint('routes', __name__)
db = Database() # Instância local para as rotas

@routes_bp.route('/usuarios', methods=['POST'])
def criar_cadastro():
    db.conectar
    try:
        dados_recebidos = request.get_json()
        dados_obrigatorios = ['nome_completo', 'email', 'senha', 'whatsapp']

        if not all(dados in dados_recebidos for dados in dados_obrigatorios):
            return jsonify({'erro': 'Faltam campos obrigatórios'}), 400

        sql_verifica_email = 'SELECT * FROM usuarios WHERE email = %s'
        email_ja_cadastrado = db.obter_dados(sql_verifica_email, (dados_recebidos['email'],))

        if email_ja_cadastrado:
            return jsonify({'erro': 'Email já cadastrado!'}), 401

        sql_verifica_whatsapp = 'SELECT * FROM usuarios WHERE whatsapp = %s'
        whatsapp_ja_cadastrado = db.obter_dados(sql_verifica_whatsapp, (dados_recebidos['whatsapp'],))

        if whatsapp_ja_cadastrado:
            return jsonify({'erro': 'Whatsapp já cadastrado!'}), 401

        senha_bytes = dados_recebidos['senha'].encode('utf-8')
        senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())

        sql_guardar_dados = """
        INSERT INTO usuarios (nome_completo, email, senha, whatsapp)
        VALUES (%s, %s, %s, %s)
        """
        valores = (
            dados_recebidos['nome_completo'],
            dados_recebidos['email'],
            senha_hash,
            dados_recebidos['whatsapp']
        )

        resultado = db.executar_query(sql_guardar_dados, valores)

        if resultado:
            return jsonify({'mensagem': 'Cadastro concluido com sucesso!'}), 200
        else:
            return jsonify({'erro': 'Cadastro não finalizado!'}), 500
    except Exception as erro:
        return jsonify({'erro': str(erro)}), 500