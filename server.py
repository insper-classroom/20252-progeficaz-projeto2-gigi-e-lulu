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
# Listar todos os imóveis

# -------------------------------------------------------------------------------------------------------
# Listar um imóvel específico, via id

# -------------------------------------------------------------------------------------------------------
# Adicionar um novo imóvel

# -------------------------------------------------------------------------------------------------------
# Atualizar um imóvel existente

# -------------------------------------------------------------------------------------------------------
# Remover um imóvel existente

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade 

# -------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)