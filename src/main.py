from flask import Flask
import os
from dotenv import load_dotenv

# ⬇️ Adicione essas duas linhas:
from src.automacao import cron_lead_scanning

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return 'JGNEXT Afiliados rodando com sucesso no Render!'

# ⬇️ NOVA ROTA AQUI
@app.route('/agente-captacao')
def agente_captacao():
    cron_lead_scanning.run()
    return 'Agente de Captação executado com sucesso.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

