import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os
from dotenv import load_dotenv

# Carregar .env mesmo executando fora da pasta
ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

DB_CONFIG = {
    'host': os.getenv("MYSQL_HOST"),
    'port': int(os.getenv("MYSQL_PORT")),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}


def conectar_bd():
    """Conecta ao banco e retorna a conexão."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao BD: {e}")
        print("DEBUG CONFIG:", DB_CONFIG)
        return None


# ---------- Histórico ----------
def salvar_historico(role, mensagem):
    conn = conectar_bd()
    if not conn:
        return
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "INSERT INTO historico (role, content, timestamp) VALUES (%s, %s, %s)",
            (role, mensagem, datetime.now())
        )
        conn.commit()
    except Error as e:
        print(f"Erro ao salvar histórico: {e}")
    finally:
        cursor.close()
        conn.close()


def buscar_historico():
    conn = conectar_bd()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM historico ORDER BY timestamp ASC")
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao buscar histórico: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def limpar_historico():
    conn = conectar_bd()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM historico")
        conn.commit()
    except Error as e:
        print(f"Erro ao limpar histórico: {e}")
    finally:
        cursor.close()
        conn.close()


# ---------- Produtos ----------
def buscar_produto(query):
    conn = conectar_bd()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    try:
        like = f"%{query}%"
        cursor.execute(
            "SELECT * FROM produtos WHERE nome LIKE %s OR marca LIKE %s",
            (like, like)
        )
        return cursor.fetchall()
    except Error as e:
        print(f"Erro ao buscar produto: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
