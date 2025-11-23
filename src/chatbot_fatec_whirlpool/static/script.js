const chatForm = document.getElementById("chat-form");
const chatBox = document.getElementById("chat-box");
const ragBtn = document.getElementById("rag-btn");
const historicoBtn = document.getElementById("historico-btn");

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const mensagemInput = document.getElementById("mensagem");
    const mensagem = mensagemInput.value.trim();
    if (!mensagem) return;

    appendMessage("Você", mensagem);
    mensagemInput.value = "";

    const response = await fetch("/get_response", {
        method: "POST",
        body: new URLSearchParams({ mensagem }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    });
    const respostaText = await response.text();
    appendMessage("Bot", respostaText);
});

ragBtn.addEventListener("click", async () => {
    const mensagemInput = document.getElementById("mensagem");
    const mensagem = mensagemInput.value.trim();
    if (!mensagem) return;

    appendMessage("Você (RAG)", mensagem);
    mensagemInput.value = "";

    const response = await fetch("/get_rag_response", {
        method: "POST",
        body: new URLSearchParams({ mensagem }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    });
    const respostaText = await response.text();
    appendMessage("RAG", respostaText);
});

historicoBtn.addEventListener("click", () => {
    window.location.href = "/historico";
});

function appendMessage(sender, message) {
    const p = document.createElement("p");
    p.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(p);
    chatBox.scrollTop = chatBox.scrollHeight;
}
