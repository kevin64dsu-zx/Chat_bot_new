import mysql.connector
from mysql.connector import Error
from datetime import datetime
import os
from dotenv import load_dotenv
import requests
import numpy as np
from typing import List, Dict, Optional

# Carregar .env mesmo executando fora da pasta
ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(ENV_PATH)

# ==========================================================
# CONFIGURAÇÃO GERAL
# ==========================================================
DB_CONFIG = {
    'host': os.getenv("MYSQL_HOST"),
    'port': int(os.getenv("MYSQL_PORT")),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}

# --- CONFIGURAÇÃO GEMINI (RAG) ---
API_KEY = os.getenv("GEMINI_API_KEY") # Chave da API do Gemini
EMBEDDING_MODEL = "text-embedding-004"
EMBEDDING_DIMENSION = 768 # Dimensão do vetor (embedding) para o modelo 'text-embedding-004'

if not API_KEY:
    print("ERRO: GEMINI_API_KEY não encontrada no arquivo .env.")

# ==========================================================
# FUNÇÕES DE UTILIDADE E CONEXÃO
# ==========================================================

def conectar_bd():
    """Conecta ao banco e retorna a conexão."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Erro ao conectar ao BD: {e}")
        print("DEBUG CONFIG:", DB_CONFIG)
        return None

# ==========================================================
# FUNÇÕES DO GEMINI E EMBEDDING
# ==========================================================

def calculate_embedding(text: str) -> Optional[List[float]]:
    """Calcula o vetor (embedding) para um texto usando a API do Gemini."""
    if not API_KEY:
        return None
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{EMBEDDING_MODEL}:embedContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "content": {
            "parts": [{"text": text}]
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        data = response.json()
        
        # O resultado do embedding vem dentro da estrutura
        embedding_data = data.get('embedding', {}).get('values', [])
        
        if embedding_data:
            return embedding_data
        else:
            print("Erro: API não retornou embedding válido.")
            return None
            
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao calcular embedding: {e.response.status_code} - {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de Requisição ao calcular embedding: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado ao calcular embedding: {e}")
        return None


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Calcula a similaridade de cosseno entre dois vetores NumPy."""
    # O produto escalar dos vetores (dot product)
    dot_product = np.dot(v1, v2)
    # A norma (magnitude) dos vetores
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    # Evita divisão por zero
    if norm_v1 == 0 or norm_v2 == 0:
        return 0.0
        
    return dot_product / (norm_v1 * norm_v2)


# ==========================================================
# FUNÇÕES RAG (Busca Vetorial)
# ==========================================================

def buscar_documentos_relevantes_rag(query: str, top_k: int = 3) -> List[str]:
    """
    Realiza a busca vetorial (RAG) no banco de dados para encontrar os 
    documentos mais semanticamente relevantes para a query.
    Retorna uma lista de strings (o conteúdo dos chunks).
    """
    
    # 1. Calcular o embedding da pergunta do usuário
    query_vector = calculate_embedding(query)
    if not query_vector:
        return []
    
    query_vector_np = np.array(query_vector)
    
    conn = conectar_bd()
    if not conn:
        return []

    relevantes = []
    
    # 2. Buscar todos os documentos e seus vetores no MySQL
    cursor = conn.cursor(dictionary=True)
    try:
        # Pega o id, o texto (chunk) e o vetor
        cursor.execute("SELECT id, content_chunk, embedding_vector FROM rag_documents")
        documents = cursor.fetchall()
        
        if not documents:
            print("AVISO: Tabela rag_documents está vazia. Rode o script de indexação.")
            return []

        # 3. Calcular a similaridade para CADA documento
        similarities = []
        for doc in documents:
            # O vetor está salvo no DB como uma string JSON, precisamos converter para NumPy
            try:
                doc_vector = np.array(eval(doc['embedding_vector']))
            except:
                print(f"Erro ao processar vetor ID {doc['id']}. Pulando.")
                continue

            similarity = cosine_similarity(query_vector_np, doc_vector)
            similarities.append({
                'content': doc['content_chunk'],
                'similarity': similarity
            })

        # 4. Ordenar e selecionar os Top K mais relevantes
        similarities.sort(key=lambda x: x['similarity'], reverse=True)
        
        # 5. Formatar a lista de retorno
        relevantes = [item['content'] for item in similarities[:top_k]]
        
    except Error as e:
        print(f"Erro ao buscar documentos RAG: {e}")
    finally:
        cursor.close()
        conn.close()
        
    return relevantes


# ==========================================================
# FUNÇÃO DE INDEXAÇÃO (Para uso na população da base)
# ==========================================================

def indexar_chunk_rag(chunk: str, source: str) -> bool:
    """
    Calcula o embedding de um chunk de texto e o salva na tabela rag_documents.
    Esta função será chamada pelo script de indexação.
    """
    vector = calculate_embedding(chunk)
    if not vector:
        return False
        
    # Converte a lista de floats do vetor em uma string que o MySQL pode armazenar
    # Usaremos repr() para garantir que a lista seja salva de forma segura
    vector_str = repr(vector)

    conn = conectar_bd()
    if not conn:
        return False
        
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO rag_documents (content_chunk, embedding_vector, source_document) VALUES (%s, %s, %s)",
            (chunk, vector_str, source)
        )
        conn.commit()
        return True
    except Error as e:
        print(f"Erro ao indexar chunk: {e}")
        return False
    finally:
        cursor.close()
        conn.close()


# ==========================================================
# FUNÇÕES DE HISTÓRICO E PRODUTOS (EXISTENTES)
# ==========================================================

# O restante das suas funções (salvar_historico, buscar_historico, limpar_historico, buscar_produto)
# permanecem inalteradas abaixo para manter a compatibilidade.

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