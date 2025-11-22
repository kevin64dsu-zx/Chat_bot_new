import os
from google import genai
from db_connector import salvar_historico, buscar_historico

# ====== INSTRUÇÃO DE SISTEMA (PERSONALIDADE DO BOT) ======
SYSTEM_INSTRUCTION = """
Você é o Assistente Virtual Oficial do Grupo Whirlpool (Brastemp, Consul, KitchenAid).
Suas diretrizes de resposta são:
1. Responda de forma CURTA, AMIGÁVEL e OBJETIVA. Nunca escreva parágrafos longos.
2. Use emojis moderadamente (😊, 🔧, 🧊) para dar um toque de carisma.
3. Se perguntarem algo fora do escopo (ex: política), peça desculpas e redirecione para o suporte técnico.
4. Nunca saia do personagem. Você trabalha para a Whirlpool.
"""

# inicializa cliente
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Usamos a versão mais estável e moderna do modelo
MODEL_NAME = "gemini-2.5-flash"

# FUNÇÃO AUXILIAR PARA CORRIGIR O NOME DA FUNÇÃO
def map_role(role_db):
    """Mapeia o role 'assistant' (do DB) para 'model' (da API Gemini)."""
    if role_db == "assistant":
        return "model"
    return role_db # Retorna 'user' ou outros sem alteração

def gerar_resposta_usuario(mensagem):
    try:
        mensagem_a_enviar = str(mensagem)
        
        # 1. RECUPERA O HISTÓRICO COMPLETO DO BANCO DE DADOS
        historico_db = buscar_historico()
        
        # 2. MONTA A LISTA DE 'CONTENTS' PARA O GEMINI
        contents = []
        for item in historico_db:
            conteudo = item.get("content", "")
            if conteudo: # Adiciona apenas se houver conteúdo
                contents.append({
                    # CORREÇÃO CRUCIAL: USANDO map_role AQUI!
                    "role": map_role(item["role"]), 
                    "parts": [{"text": conteudo}]
                })
            
        # 3. ADICIONA A NOVA MENSAGEM DO USUÁRIO
        contents.append({
            "role": "user", 
            "parts": [{"text": mensagem_a_enviar}]
        })
        
        # 4. CHAMA O MODELO COM O HISTÓRICO E A INSTRUÇÃO DE SISTEMA
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents, # O histórico completo
            config={"system_instruction": SYSTEM_INSTRUCTION} # A nova personalidade!
        )

        resposta_texto = response.text.strip()

        # 5. Salva a nova rodada (mantendo 'assistant' para o DB)
        salvar_historico("user", mensagem_a_enviar)
        salvar_historico("assistant", resposta_texto)

        return resposta_texto

    except Exception as e:
        print("Erro IA:", e)
        return "Desculpe, a IA está com problemas de comunicação. Verifique sua chave de API."

def obter_historico():
    try:
        return buscar_historico()
    except Exception as e:
        print("Erro ao buscar histórico:", e)
        return []