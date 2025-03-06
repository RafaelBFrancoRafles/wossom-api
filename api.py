from flask import Flask, jsonify
import gspread
import json
import os
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Load credentials from Render environment variables
json_key = json.loads(os.environ["GOOGLE_CREDENTIALS"])
creds = Credentials.from_service_account_info(json_key, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

# Open Google Sheet
SHEET_NAME = "venda ap"  # Change if using a different sheet
sheet = client.open(SHEET_NAME).sheet1

# Define expected headers for clean data retrieval
expected_headers = [
    'Rentabilidade prevista (sem descontar inflação)', 
    'Despesas atuais do apartamento', 
    'Inflação prevista (12 meses)', 
    'Gasto extra reinvestido (cenário 2)', 
    'Valor de venda do apartamento', 
    'Anos pra compensar', 
    'Valor restante após dívida (1)', 
    'Mensal', 
    'Rendimento mensal após compensação', 
    'A', 'B', 
    'Anos decorridos', 
    'Meses decorridos', 
    'Rendimento mensal', 
    'Condomínio ajustado pela inflação', 
    'Gasto extra reinvestido (corrigido inflação)', 
    'Soma rendimento + gastos evitados', 
    'Inflação incidente sobre rendimento + gastos evitados', 
    'Valor restante após dívida (2)', 
    'Valorização do apartamento (inflação)', 
    'Saldo acumulado', 
    'Diferença'
]

@app.route("/get_data", methods=["GET"])
def get_data():
    """API endpoint to fetch Google Sheets data."""
    data = sheet.get_all_records(expected_headers=expected_headers)
    return jsonify(data)

# Run the API with correct port binding for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get Render's port, default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
