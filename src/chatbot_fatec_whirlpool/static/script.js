function enviar() {
    const input = document.getElementById("input");
    const mensagem = input.value.trim();
    if (!mensagem) return;

    const chat = document.getElementById("chat");
    const usuarioDiv = document.createElement("div");
    usuarioDiv.className = "user-msg";
    usuarioDiv.textContent = mensagem;
    chat.appendChild(usuarioDiv);

    fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `mensagem=${encodeURIComponent(mensagem)}`
    })
    .then(res => res.text())
    .then(data => {
        const iaDiv = document.createElement("div");
        iaDiv.className = "ia-msg";
        iaDiv.textContent = data;
        chat.appendChild(iaDiv);
        chat.scrollTop = chat.scrollHeight;
    });

    input.value = "";
}
