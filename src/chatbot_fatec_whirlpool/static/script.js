function enviar() {
    const input = document.getElementById("input");
    const mensagem = input.value.trim();
    if (!mensagem) return;

    const chat = document.getElementById("chat");
    const typingIndicator = document.getElementById("typing-indicator");
    
    // 1. ADICIONA MENSAGEM DO USUÁRIO
    adicionarMensagem(chat, mensagem, 'user');

    input.value = "";
    
    // 2. MOSTRA O INDICADOR DE DIGITAÇÃO
    typingIndicator.style.display = 'flex';
    chat.scrollTop = chat.scrollHeight; // Rola para o indicador

    fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `mensagem=${encodeURIComponent(mensagem)}`
    })
    .then(res => res.text())
    .then(data => {
        // 3. ESCONDE O INDICADOR
        typingIndicator.style.display = 'none';
        
        // 4. ADICIONA MENSAGEM DO BOT
        adicionarMensagem(chat, data, 'bot');
    })
    .catch(error => {
        // ESCONDE O INDICADOR MESMO EM CASO DE ERRO
        typingIndicator.style.display = 'none';
        console.error('Erro ao buscar resposta do bot:', error);
        adicionarMensagem(chat, "Desculpe, não consegui conectar ao servidor.", 'bot');
    });
}

function adicionarMensagem(chatElement, texto, remetente) {
    const messageRow = document.createElement("div");
    messageRow.className = `message ${remetente}`; 

    // NOVO: Criamos um span para o emoji em vez de uma tag img
    const avatar = document.createElement("span");
    avatar.className = "avatar-emoji"; // Nova classe para estilização de emoji

    if (remetente === 'user') {
        avatar.textContent = "🧑‍💻"; // Emoji para Usuário
    } else {
        avatar.textContent = "🤖"; // Emoji para Bot
    }

    const contentDiv = document.createElement("div");
    contentDiv.className = "message-content";
    contentDiv.textContent = texto;
    
    messageRow.appendChild(avatar);
    messageRow.appendChild(contentDiv);
    
    chatElement.appendChild(messageRow);
    chatElement.scrollTop = chatElement.scrollHeight;
}

document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('input');
    inputField.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); 
            enviar();
        }
    });
});