from flask import Flask, jsonify, request
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__)

# Conexão com o banco de dados SQL
db_config = {
    "host": os.getenv("HOST"),
    "port": int(os.getenv("PORT")),
    "user": os.getenv("USER"),
    "password": os.getenv("PASSWORD"),
    "database": os.getenv("DB"),
    "ssl_ca": "ca.pem"
}

def conectando_db():
    return mysql.connector.connect(**db_config)

@app.route("/")
def home():
    return jsonify({"mensagem": "API funcionando!"})


# -------------------------------------------------------------------------------------------------------
# Listar todos os imóveis - GET - /imoveis

# -------------------------------------------------------------------------------------------------------
# Listar um imóvel específico, via id - GET - /imoveis/<id>

# -------------------------------------------------------------------------------------------------------
# Adicionar um novo imóvel - POST - /imoveis

# -------------------------------------------------------------------------------------------------------
# Atualizar um imóvel existente - PUT - /imoveis/<id>

# -------------------------------------------------------------------------------------------------------
# Remover um imóvel existente - DELETE - /imoveis/<id>

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo - GET - /imoveis/tipo/<tipo>

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade - GET - /imoveis/cidade/<cidade>

# -------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)