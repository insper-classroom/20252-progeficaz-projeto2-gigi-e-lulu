# CRIAR TODAS AS FUNÇÕES COM "db" NO FINAL PARA DIFERENCIAR DAS DO SERVER.PY, EVITANDO CONFUSÃO !!!!!!!!!!!!

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

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