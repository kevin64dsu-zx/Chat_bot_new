from flask import Flask, request, render_template, redirect, url_for
from port_ia import gerar_resposta_usuario, obter_historico
from db_connector import limpar_historico  # função que vamos criar no DB se não existir

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    mensagem_usuario = request.form.get("mensagem")
    if not mensagem_usuario:
        return "Mensagem vazia!", 400
    resposta = gerar_resposta_usuario(mensagem_usuario)
    return resposta

@app.route("/historico")
def historico():
    historico_lista = obter_historico()
    return render_template("history.html", history=historico_lista)

@app.route("/limpar_historico", methods=["POST"])
def limpar_historico_route():
    limpar_historico()
    return redirect(url_for("historico"))

if __name__ == "__main__":
    app.run(debug=True)
