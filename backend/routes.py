from flask import Flask, request, jsonify
from models import db
from flask_cors import CORS
from app import app

# - Quando o frontend envia dados, você precisa de `request` para pegar
# - Quando você retorna dados, precisa de `jsonify` para transformar 

@app.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    try:
        # PEGA OS DADOS QUE O FRONTEND ENVIOU
        dados = request.get_json()

        # VALIDA SE TODOS OS CAMPOS FORMA ENVIADOS
        campos_obrigatorios = ['nome', 'telefone', 'data', 'hora', 'barbeiro', 'corte']
        if not all(campo in dados for campo in campos_obrigatorios):
            return jsonify({'erro': 'Faltam campos obrigatórios'}), 400
        
        # QUERY SQL PARA INSERIR NO BANCO
        query =  """
        INSERT INTO agendamentos (nome, telefone, data, hora, barbeiro, corte)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        #DADOS QUE VÃO SER INSERIDOS
        valores = (
            dados['nome'],
            dados['telefone'],
            dados['data'],
            dados['hora'],
            dados['barbeiro'],
            dados['corte']
        )

        #EXECUTA A QUERY
        if db.executar_query(query, valores):
            return jsonify({'mensagem': 'Agendamento criado com sucesso!'}), 201
        else:
            return jsonify({'erro': 'Erro ao criar agendamento'}), 500
    
    except Exception as erro:
        return jsonify({'erro': str(erro)}), 500



@app.route('/agendamentos', methods=['GET'])
def listar_agendamento():
    #LISTA TODOS OS AGENDAMENTOS
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