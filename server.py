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
@app.route('imoveis/<id>', methods=['GET'])
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
def atualizar_imovel()
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400 # não processa o bad request

    if not db.buscar_imovel_db(id)
        return jsonify({"erro": "Imóvel não encontrado"}), 404 # página não encontrada

    db.atualizar_imovel_db(id, dados)
    return jsonify({"mensagem": "Imóvel atualizado com sucesso"}), 200 # solicitação bem sucedida

# -------------------------------------------------------------------------------------------------------
# Remover um imóvel existente - DELETE - /imoveis/<id>

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo - GET - /imoveis/tipo/<tipo>

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade - GET - /imoveis/cidade/<cidade>

# -------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)