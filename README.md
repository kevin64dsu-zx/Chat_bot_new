# 🤖 Chatbot Whirlpool: Assistente Virtual Inteligente (Versão Estável)

## Visão Geral do Projeto

Este projeto consiste no desenvolvimento de um chatbot inteligente para auxiliar clientes com dúvidas sobre produtos Whirlpool (máquinas de lavar, fogões, etc.). O assistente utiliza Processamento de Linguagem Natural (PLN) para interpretar as perguntas dos usuários e gerar respostas relevantes, simulando uma interação humana.

Esta versão é a **implementação estável** que integra o modelo Google Gemini com persistência de histórico em banco de dados MySQL.

## ⚙️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask
* **Inteligência Artificial:** API do Google Gemini (gemini-2.5-flash)
* **Banco de Dados:** MySQL (para histórico de conversas)
* **Gerenciamento de Dependências:** `pip` e `requirements.txt`

---

## 🚀 Como Rodar o Projeto (Deploy Local)

Esta versão é projetada para rodar diretamente em um ambiente Python.

### Pré-requisitos

1.  **Python 3.9+** instalado.
2.  **MySQL Server** rodando (na porta 3306, se o `db_connector.py` usar `localhost`).
3.  **Chave de API:** Uma chave ativa do Google Gemini.

### 1. Configuração do Ambiente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/kevin64dsu-zx/Chat_bot_new.git](https://github.com/kevin64dsu-zx/Chat_bot_new.git)
    cd Chat_bot_new
    ```
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure o Ambiente:**
    Crie um arquivo na raiz do projeto chamado **`.env`** e insira sua chave de API e as credenciais do banco de dados (os nomes das variáveis devem ser os mesmos usados no `db_connector.py` e `port_ia.py`):
    ```env
    # Exemplo do arquivo .env
    GOOGLE_API_KEY="SUA_CHAVE_DO_GEMINI_AQUI"
    # Adicione as credenciais do MySQL se forem usadas no código (ex: USER, PASSWORD, HOST)
    ```

### 2. Execução

Execute o arquivo principal para iniciar o servidor Flask:

```bash
python seu_arquivo_principal.py # (Substitua pelo nome do seu arquivo Flask, geralmente 'app.py')