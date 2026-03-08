from flask import Flask, request, jsonify
from models import db
from flask_cors import CORS
from app import app
import bcrypt

# - Quando o frontend envia dados, você precisa de `request` para pegar
# - Quando você retorna dados, precisa de `jsonify` para transformar


@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    try:
        # PEGA OS DADOS QUE O FRONTEND ENVIOU
        dados = request.get_json()

        # VALIDA SE TODOS OS CAMPOS FORAM ENVIADOS
        campos_obrigatorios = ['nome', 'telefone',
                               'data', 'hora', 'barbeiro', 'corte']
        if not all(campo in dados for campo in campos_obrigatorios):
            return jsonify({'erro': 'Faltam campos obrigatórios'}), 400

        # QUERY SQL PARA INSERIR NO BANCO
        query = """
        INSERT INTO agendamentos (nome, telefone, data, hora, barbeiro, corte)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        # DADOS QUE VÃO SER INSERIDOS
        valores = (
            dados['nome'],
            dados['telefone'],
            dados['data'],
            dados['hora'],
            dados['barbeiro'],
            dados['corte']
        )

        # EXECUTA A QUERY
        if db.executar_query(query, valores):
            return jsonify({'mensagem': 'Agendamento criado com sucesso!'}), 201
        else:
            return jsonify({'erro': 'Erro ao criar agendamento'}), 500

    except Exception as erro:
        return jsonify({'erro': str(erro)}), 500


@app.route('/agendamentos', methods=['GET'])
def listar_agendamento():
    # LISTA TODOS OS AGENDAMENTOS
    try:
        query = 'SELECT * FROM agendamentos'
        agendamentos = db.obter_dados(query)

        if agendamentos:
            return jsonify(agendamentos), 200
        else:
            return jsonify([]), 200

    except Exception as erro:
        return jsonify({'erro': str(erro)}), 500


@app.route('/agendamentos/<id>', methods=['DELETE'])
def deletar_agendamento(id):
    # DELETE UM AGENDAMENTO PELO ID
    try:
        query = 'DELETE FROM agendamentos WHERE id = %s'

        if db.executar_query(query, (id,)):
            return jsonify({'mensagem': 'Agendamento deletado com sucesso!'}), 200
    except Exception as erro:
        return jsonify({'erro': str(erro)}), 500


""" CRIAR NOVO USUÁRIO """


@app.route('/usuarios', methods=['POST'])
def criar_novo_usuario():
    try:
        # PEGA OS DADOS QUE O FRONTEND ENVIOU
        dadosParaCadastro = request.get_json()

        # VALIDA SE TODOS OS CAMPOS FORAM ENVIADOS
        campos_obrigadorios = ['nome_completo', 'email', 'senha', 'whatsapp']

        if not all(campo in dadosParaCadastro for campo in campos_obrigadorios):
            return jsonify({'erro': 'Faltam campos obrigartórios'}), 400

        # VERIFICA SE EMAIL E WHATSAPP JÁ FORAM CADASTRADOS
        query_verificar_email = 'SELECT * FROM usuarios WHERE email = %s'
        email_existente = db.obter_dados(query_verificar_email, (dadosParaCadastro['email'],))

        query_verificar_whatsapp = 'SELECT * FROM usuarios WHERE whatsapp = %s'
        whatsapp_existente = db.obter_dados(query_verificar_whatsapp, (dadosParaCadastro['whatsapp'],))

        if email_existente:
            return jsonify({'Erro': 'Email já cadastrado!'}), 400

        elif whatsapp_existente:
            return jsonify({'Erro': 'Whatsapp já cadastrado!'}), 400

        # CRIA UMA VARIÁVEL E RECEBE A SENHA QUE O USUÁRIO DIGITOU E TRANSFORMA ELA EM BYTES
        senha_bytes = dadosParaCadastro['senha'].encode('utf-8')

        # PEGA A SENHA QUE JÁ ESTA TRANSFORMADA EM BYTES E SALVA NA VARIÁVEL SENHA_BYTES E TRANSFORMA EM HASH SALVANDO EM UMA NOVA VARIÁVEL PARA ENVIAR PRO BANCO DE DADOS
        senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())

        # QUEY SQL PARA INSERIR NO BANCO
        query = """
        INSERT INTO usuarios (nome_completo, email, senha, whatsapp)
        VALUES (%s, %s, %s, %s)
        """
        # DADOS QUE VÃO SER INSERIDOS
        valores = (
            dadosParaCadastro['nome_completo'],
            dadosParaCadastro['email'],
            senha_hash,
            dadosParaCadastro['whatsapp']
        )

        if db.executar_query(query, valores):
            return jsonify({'Mensagem': 'A conta do usuário foi criada com sucesso!'}), 201
        else:
            return jsonify({'Erro': 'Erro ao criar a conta de usuário!'})
    except Exception as erro:
        return jsonify({'Erro': str(erro)}), 500


""" VALIDAR LOGIN NO BANCO DE DADOS """


@app.route('/login', methods=['POST'])
def fazer_login():
    try:
        dadosParaLogin = request.get_json()

        campos_obrigatorios = ['email', 'senha']
        if not all(campo in dadosParaLogin for campo in campos_obrigatorios):
            return jsonify({'erro': 'Faltam campos obrigatórios'}), 400

        query_verificar_email = 'SELECT * FROM usuarios WHERE email = %s'
        email_existente = db.obter_dados(query_verificar_email, (dadosParaLogin['email'],))

        if not email_existente:
            return jsonify({'Erro': 'Email não cadastrado!'}), 400

        senha_bytes = dadosParaLogin['senha'].encode('utf-8')
        usuario = email_existente[0]
        hash_do_banco_de_dados = usuario['senha'].encode('utf-8')
        senha_usuario = bcrypt.checkpw(senha_bytes, hash_do_banco_de_dados)

        if senha_usuario:
            return jsonify({'Mensagem': 'Login realizado com sucesso!'}), 200
        else:
            return jsonify({'Erro': 'Senha incorreta!'}), 400

    except Exception as erro:
        return jsonify({'Erro': str(erro)}), 500