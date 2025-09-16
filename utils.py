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
def listar_imoveis_db():
    conn = conectando_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM imoveis")
    imoveis = cursor.fetchall()
    conn.close()
    return imoveis
            
# -------------------------------------------------------------------------------------------------------
# Listar um imóvel específico, via id 
def buscar_imovel_db(id):
    conn = conectando_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM imoveis WHERE id = %s", (id,))
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
def atualizar_imovel_db(id, dados):
    conn = conectando_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE imoveis SET logradouro=%s, tipo_logradouro=%s, bairro=%s, cidade=%s,
        cep=%s, tipo=%s, valor=%s, data_aquisicao=%s WHERE id=%s
    """, (
        dados["logradouro"], dados["tipo_logradouro"], dados["bairro"], 
        dados["cidade"], dados["cep"], dados["tipo"], 
        dados["valor"], dados["data_aquisicao"], id
    ))
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------------------------------------
# Remover um imóvel existente
def remover_imovel_db(id):
    conn = conectando_db()
    sql = "DELETE FROM imoveis WHERE id = %s"
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (id,))
            conn.commit()
            return cur.rowcount > 0
    finally:
        conn.close()
# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo
def listar_imovel_por_tipo_db(tipo):
    sql = "SELECT * FROM imoveis WHERE tipo = %s"
    conn = conectando_db()
    try:
        with conn.cursor() as cur:
            cur.execute(sql,(id,))
            conn.commit()
            return cur.rowcount > 0 
    finally :
        conn.close()
# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade 
def listar_imovel_por_cidade_db(cidade):
    sql= "SELECT * FROM imoveis WHERE tipo = %s "
    conn = conectando_db()
    try:
        with conn.cursor() as cur :
            cur.execute(sql,(id, ))
            conn.commit()
        return cur.rowcount> 0
    finally : 
        conn.close()
# -------------------------------------------------------------------------------------------------------