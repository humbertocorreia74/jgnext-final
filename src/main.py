from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "JGNEXT Afiliados rodando com sucesso no Render!"
