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

###PRECISAMOS ESTABELECER UM CONN
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
def remover_imovel_db(id: int) -> bool:
    sql = "DELETE FROM imoveis WHERE id = %s"
    conn = _get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (id,))
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()
# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo - GET - /imoveis/tipo/<tipo>

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade - GET - /imoveis/cidade/<cidade>

# -------------------------------------------------------------------------------------------------------