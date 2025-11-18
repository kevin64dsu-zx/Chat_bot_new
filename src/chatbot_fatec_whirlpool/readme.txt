# 🤖 Chatbot Whirlpool (MVP) - Fatec

Este projeto consiste no desenvolvimento de um **Assistente Virtual Inteligente** focado no atendimento ao cliente das marcas do grupo Whirlpool (Brastemp, Consul, KitchenAid).

O objetivo é entregar um MVP (Produto Mínimo Viável) que utilize **Inteligência Artificial Generativa** para responder dúvidas sobre produtos, manuais e suporte técnico, oferecendo uma experiência de usuário moderna e eficiente.

---

## 👥 Autoria

**Desenvolvido por:** Grupo 3 & Kevin
**Instituição:** Fatec (Projeto Semestral)

---

## 🚀 Funcionalidades Atuais

* **Interface de Chat Interativa:** Layout moderno com diferenciação visual clara entre mensagens do Usuário e do Assistente.
* **Histórico de Conversas:** Capacidade de visualizar interações passadas.
* **Personalização:** Suporte a **Modo Escuro (Dark Mode)** e **Modo Claro**, além de ajustes de fonte.
* **Usabilidade:** Envio de mensagens via tecla `Enter` e feedback visual.
* **Backend Flask:** Servidor Python robusto para gerenciamento das rotas e lógica de resposta.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Web:** Flask
* **Front-end:** HTML5, CSS3, JavaScript
* **Controle de Versão:** Git & GitHub

---

## 🔮 Roadmap (Próximos Passos)

* [ ] **Integração RAG (Retrieval-Augmented Generation):** Implementação de base de conhecimento com manuais e fichas técnicas dos produtos.
* [ ] **Branding Whirlpool:** Inserção de logotipos e identidade visual das marcas (Brastemp, Consul).
* [ ] **Widgets Sazonais:** Elementos interativos (ex: Relógio, Contagem Regressiva) para humanizar a interface.
* [ ] **Busca Web:** Integração de ferramentas para busca de informações externas em tempo real.

---

## 📦 Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/kevin64dsu-zx/Chat_bot_new.git](https://github.com/kevin64dsu-zx/Chat_bot_new.git)
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    # Navegue até a pasta do app se necessário
    python src/chatbot_fatec_whirlpool/app.py
    ```

5.  **Acesse no navegador:**
    `http://127.0.0.1:5000`

---