from flask import Flask, request, jsonify
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets Setup
import json
import os
from google.oauth2.service_account import Credentials
from flask import Flask, jsonify
import gspread

app = Flask(__name__)

# Load credentials from Render environment variables
json_key = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(json_key, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

SHEET_NAME = "venda ap"  # Change if using a different sheet
sheet = client.open(SHEET_NAME).sheet1

@app.route("/get_data", methods=["GET"])
def get_data():
    """API endpoint to fetch Google Sheets data."""
    data = sheet.get_all_records()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

client = gspread.authorize(creds)

SHEET_NAME = "venda ap"  # Change to your actual sheet name
sheet = client.open(SHEET_NAME).sheet1

# Define unique headers (same as before)
expected_headers = ['Rentabilidade prevista (sem descontar inflação)', 'Despesas atuais do apartamento', 'Inflação prevista (12 meses)', 'Gasto extra reinvestido (cenário 2)', 'Valor de venda do apartamento', 'Anos pra compensar', 'Valor restante após dívida (1)', 'Mensal', 'Rendimento mensal após compensação', 'A', 'B', 'Anos decorridos', 'Meses decorridos', 'Rendimento mensal', 'Condomínio ajustado pela inflação', 'Gasto extra reinvestido (corrigido inflação)', 'Soma rendimento + gastos evitados', 'Inflação incidente sobre rendimento + gastos evitados', 'Valor restante após dívida (2)', 'Valorização do apartamento (inflação)', 'Saldo acumulado', 'Diferença']

@app.route("/get_data", methods=["GET"])
def get_data():
    """API endpoint to fetch Google Sheets data."""
    data = sheet.get_all_records(expected_headers=expected_headers)
    return jsonify(data)

# Run the API
if __name__ == "__main__":
    app.run(port=5000, debug=True)
