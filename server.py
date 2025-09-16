from flask import Flask, jsonify, request
import utils as db

app = Flask(__name__)

# -------------------------------------------------------------------------------------------------------
# Listar todos os imóveis
@app.route("/imoveis", methods=["GET"])
def listar_imoveis():
    try:
        return jsonify(db.listar_imoveis_db()), 200 # solicitação bem sucedida
    except Exception as e:
        return jsonify({"erro": str(e)}), 500 # erro interno do servidor

# -------------------------------------------------------------------------------------------------------
# Listar um imóvel específico, via id
@app.route('/imoveis/<id>', methods=['GET'])
def buscar_imovel():
    imovel = db.buscar_imovel_db(id)
    if imovel: # se ele for encontrado é True
        return jsonify(imovel), 200 # solicitação bem sucedida
    return jsonify({'Erro': 'Imóvel não encontrado'}), 404 # página não encontrada

# -------------------------------------------------------------------------------------------------------
# Adicionar um novo imóvel
@app.route("/imoveis", methods=["POST"])
def adicionar_imovel():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400 # o servidor não procesa um bad request
    db.adicionar_imovel_db(dados)
    return jsonify({"mensagem": "Imóvel criado com sucesso"}), 201 # solicitação bem sucedida

# -------------------------------------------------------------------------------------------------------
# Atualizar um imóvel existente 
@app.route("/imoveis/<id>", methods=["PUT"])
def atualizar_imovel():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400 # não processa o bad request

    if not db.buscar_imovel_db(id):
        return jsonify({"erro": "Imóvel não encontrado"}), 404 # página não encontrada

    db.atualizar_imovel_db(id, dados)
    return jsonify({"mensagem": "Imóvel atualizado com sucesso"}), 200 # solicitação bem sucedida

# -------------------------------------------------------------------------------------------------------
# Remover um imóvel existente 
@app.route('/imoveis/<id>', methods=['DELETE'])
def remover_imovel(id):
    try:
        if not db.buscar_imovel_db(id):
            return jsonify({"erro": "Imóvel não encontrado"}), 404

        db.remover_imovel_db(id)
        return jsonify({"mensagem": "Imóvel removido com sucesso"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo 
@app.route("/imoveis/tipo/<string:tipo>", methods=["GET"])
def listar_por_tipo(tipo):
    try:
        imoveis = db.listar_imoveis_por_tipo_db(tipo)
        return jsonify(imoveis), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade 
@app.route("/imoveis/cidade/<string:cidade>", methods=["GET"])
def listar_por_cidade(cidade):
    try:
        imoveis = db.listar_imoveis_por_cidade_db(cidade)
        return jsonify(imoveis), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
# -------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)