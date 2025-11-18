function enviar() {
    const input = document.getElementById("input");
    const mensagem = input.value.trim();
    if (!mensagem) return;

    const chat = document.getElementById("chat");
    
    // 1. ADICIONA MENSAGEM DO USUÁRIO
    adicionarMensagem(chat, mensagem, 'user');

    // Limpa o input imediatamente após o envio
    input.value = "";

    // 2. CHAMA O BACKEND
    fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `mensagem=${encodeURIComponent(mensagem)}`
    })
    .then(res => res.text())
    .then(data => {
        // 3. ADICIONA MENSAGEM DO BOT
        adicionarMensagem(chat, data, 'bot');
    })
    .catch(error => {
        console.error('Erro ao buscar resposta do bot:', error);
        adicionarMensagem(chat, "Desculpe, houve um erro ao processar sua solicitação.", 'bot');
    });
}

// Função auxiliar para criar e anexar as mensagens
function adicionarMensagem(chatElement, texto, remetente) {
    // Cria a linha principal da mensagem (ex: <div class="message user">)
    const messageRow = document.createElement("div");
    // **USANDO AS CLASSES DO SEU CSS**
    messageRow.className = `message ${remetente}`; 

    // Cria a div de conteúdo (ex: <div class="message-content">)
    const contentDiv = document.createElement("div");
    contentDiv.className = "message-content";
    contentDiv.textContent = texto;
    
    // Anexa o conteúdo à linha da mensagem
    messageRow.appendChild(contentDiv);
    
    // Anexa a linha da mensagem à caixa de chat
    chatElement.appendChild(messageRow);
    
    // Rola para o final
    chatElement.scrollTop = chatElement.scrollHeight;
}

// ==========================================================
// FUNÇÃO ADICIONADA: Habilitar o Enter para Enviar
// ==========================================================

document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('input');
    
    // Ouvinte de evento para a tecla pressionada
    inputField.addEventListener('keypress', (event) => {
        // Verifica se a tecla pressionada é 'Enter' (código 13 ou 'Enter')
        if (event.key === 'Enter') {
            // Previne a ação padrão (quebrar linha)
            event.preventDefault(); 
            // Chama a função de envio
            enviar();
        }
    });

    // Opcional: Aqui você pode colocar o código para o botão de configurações (settings)
});