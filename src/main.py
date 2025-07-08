from flask import Flask
from src.agentes import lead_scanner_agent

app = Flask(__name__)

@app.route('/')
def index():
    return 'JGNEXT Afiliados rodando com sucesso no Render!'

@app.route('/agente-captacao')
def agente_captacao():
    lead_scanner_agent.run()  # ou execute o método correto
    return 'Agente de Captação executado com sucesso.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
