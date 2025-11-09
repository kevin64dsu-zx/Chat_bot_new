import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env

DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE'),
    'port': int(os.getenv('MYSQL_PORT')),
}

def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar no banco: {err}")
        return None

def ensure_table_exists():
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            timestamp DATETIME,
            role VARCHAR(50),
            content TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def log_message(role, content):
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    sql = "INSERT INTO chat_history (timestamp, role, content) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (datetime.now(), role, content[:5000]))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao registrar mensagem: {err}")
    finally:
        cursor.close()
        conn.close()

def get_history():
    conn = connect_db()
    if conn is None:
        return []
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT timestamp, role, content FROM chat_history ORDER BY timestamp ASC")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao recuperar histórico: {err}")
        return []
    finally:
        cursor.close()
        conn.close()

# Garante que a tabela existe ao importar o módulo
ensure_table_exists()
