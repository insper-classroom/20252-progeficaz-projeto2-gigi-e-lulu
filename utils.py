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
# Listar todos os imóveis 
def listar_imoveis_db(id):
    conn = conectando_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM imoveis")
    imoveis = cursor.fetchall()
    conn.close()
    return imoveis
            
# -------------------------------------------------------------------------------------------------------
# Listar um imóvel específico, via id 
def buscar_imovel_db():
    conn = conectando_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM imoveis WHERE id = %s", (imovel_id,))
    imovel = cursor.fetchone()
    conn.close()
    return imovel
# -------------------------------------------------------------------------------------------------------
# Adicionar um novo imóvel 
def adicionar_imovel_db(dados):
    conn = conectando_db()
    cursor = conn.cursor()
    # %s relacionado a memória que os elementos ocupam
    cursor.execute("""
        INSERT INTO imoveis (logradouro, tipo_logradouro, bairro, cidade, cep, tipo, valor, data_aquisicao)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s) 
    """, (
        dados["logradouro"], dados["tipo_logradouro"], dados["bairro"], 
        dados["cidade"], dados["cep"], dados["tipo"], 
        dados["valor"], dados["data_aquisicao"]
    ))
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------------------------------------
# Atualizar um imóvel existente 

# -------------------------------------------------------------------------------------------------------
# Remover um imóvel existente - DELETE - /imoveis/<id>
def remover_imovel_db(id: int) -> bool:
    sql = "DELETE FROM imoveis WHERE id = %s"
    conn = conectando_db
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (id,))
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()
# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo - GET - /imoveis/tipo/<tipo>
def listar_imovel_por_tipo_db(id:int, tipo: str) -> bool:
    sql = "SELECT * FROM imoveis WHERE tipo = %s"
    conn = conectando_db
    try:
        with conn.cursor() as cur:
            cur.execute(sql,(id,))
            conn.commit()
            return cur.rowcount > 0 
    finally :
        conn.close()
# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade - GET - /imoveis/cidade/<cidade>
def listar_imovel_por_cidade_db(id: int, cidade: str ):
    sql= "SELECT * FROM imoveis WHERE tipo = %s "
    conn = conectando_db
    try:
        with conn.cursor() as cur :
            cur.execute(sql,(id, ))
            conn.commit()
        return cur.rowcount> 0
    finally : 
        conn.close()
# -------------------------------------------------------------------------------------------------------