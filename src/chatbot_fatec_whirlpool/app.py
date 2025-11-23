from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, render_template, redirect, url_for
# Importa funções do seu chatbot original
from port_ia import gerar_resposta_usuario, obter_historico
from db_connector import limpar_historico 

# IMPORTAÇÃO PARA O SISTEMA RAG
# Importa as funções e o texto do relatório do novo módulo whirlpool_report_rag.py
from whirlpool_report_rag import REPORT_TEXT, get_report_chunks, retrieve_context, simulate_llm_generation

app = Flask(__name__)

# =========================================================
# 1. PRÉ-CARREGAMENTO DO CONTEXTO RAG
# Carrega e divide o relatório em 'chunks' (pedaços) assim que o servidor Flask inicia.
# Isso garante que a pesquisa (retrieval) seja instantânea.
# =========================================================
try:
    RAG_CHUNKS = get_report_chunks(REPORT_TEXT)
    print(f"Sistema RAG carregado com {len(RAG_CHUNKS)} pedaços de contexto.")
except Exception as e:
    # Caso o arquivo whirlpool_report_rag.py não esteja presente ou tenha erro
    print(f"ERRO ao carregar o sistema RAG: {e}")
    RAG_CHUNKS = []

# =========================================================
# ROTAS FLASK EXISTENTES
# =========================================================

@app.route("/")
def index():
    """Rota principal que renderiza a interface do chatbot."""
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    """Rota para o chatbot IA conversacional padrão (usando port_ia)."""
    mensagem_usuario = request.form.get("mensagem")
    if not mensagem_usuario:
        return "Mensagem vazia!", 400
    # Usa a função de IA existente para resposta conversacional
    resposta = gerar_resposta_usuario(mensagem_usuario)
    return resposta

@app.route("/historico")
def historico():
    """Rota para visualizar o histórico de conversas."""
    historico_lista = obter_historico()
    return render_template("history.html", history=historico_lista)

@app.route("/limpar_historico", methods=["POST"])
def limpar_historico_route():
    """Rota para limpar o histórico de conversas."""
    limpar_historico()
    return redirect(url_for("historico"))

# =========================================================
# 2. NOVA ROTA PARA O RAG (Retrieval-Augmented Generation)
# =========================================================

@app.route("/get_rag_response", methods=["POST"])
def get_rag_response():
    """
    Rota para o assistente de pesquisa RAG.
    Ele busca contexto no relatório e simula uma resposta do LLM.
    """
    mensagem_usuario = request.form.get("mensagem")
    if not mensagem_usuario or not RAG_CHUNKS:
        return "Nenhum contexto RAG carregado ou mensagem vazia.", 400

    # 1. Recuperação (Retrieval): Busca os trechos mais relevantes do relatório
    contexto_recuperado = retrieve_context(mensagem_usuario, RAG_CHUNKS)
    
    # 2. Geração (Generation - Simulação): Usa os trechos para gerar a resposta
    resposta_rag = simulate_llm_generation(mensagem_usuario, contexto_recuperado)
    
    # IMPORTANTE: A resposta_rag é uma string de texto formatada
    # que o seu frontend (index.html) pode exibir.
    return resposta_rag


if __name__ == "__main__":
    # CORREÇÃO DE REDE: O host='0.0.0.0' permite acesso externo.
    app.run(debug=True, host='0.0.0.0')