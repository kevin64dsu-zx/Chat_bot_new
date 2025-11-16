import os
from google import genai
from db_connector import salvar_historico, buscar_historico

# inicializa cliente
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Usamos a versão mais estável e moderna do modelo
MODEL_NAME = "gemini-2.5-flash" 

def gerar_resposta_usuario(mensagem):
    try:
        # --- SOLUÇÃO ROBUSTA DE EXTRAÇÃO DE TEXTO ---
        
        # 1. Assume que a mensagem é a string pura por padrão
        mensagem_a_enviar = str(mensagem)
        
        # 2. SE a mensagem vier como a lista/dicionário problemática 
        # (ex: [{'role': 'user', 'content': 'mensagem'}])
        if isinstance(mensagem, list) and len(mensagem) > 0:
            # Tenta extrair o 'content' do primeiro item da lista
            if isinstance(mensagem[0], dict) and 'content' in mensagem[0]:
                mensagem_a_enviar = mensagem[0]['content']
        
        # 3. Chama o modelo com a string pura e garantida
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=mensagem_a_enviar # Agora, é garantidamente uma STRING
        )

        resposta_texto = response.text.strip() # Usa strip para limpar espaços

        # salva no histórico
        salvar_historico("user", mensagem_a_enviar) # Salva a string pura
        salvar_historico("assistant", resposta_texto)

        return resposta_texto

    except Exception as e:
        print("Erro IA:", e)
        # Se a chave de API estiver errada ou a conexão falhar, este erro aparece
        return "Desculpe, a IA está com problemas de comunicação. Verifique sua chave de API."

def obter_historico():
    try:
        return buscar_historico()
    except Exception as e:
        print("Erro ao buscar histórico:", e)
        return []