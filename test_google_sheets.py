import gspread
from google.oauth2.service_account import Credentials

json_key_file = "wossom_service_account.json"
creds = Credentials.from_service_account_file(json_key_file, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

SHEET_NAME = "venda ap"  # Change if using a different sheet
sheet = client.open(SHEET_NAME).sheet1  # Open the first worksheet

# Define unique headers manually (fixing duplicates and empty values)
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
    'A',  # Renamed empty column
    'B',  # Renamed empty column
    'Anos decorridos',
    'Meses decorridos',
    'Rendimento mensal',
    'Condomínio ajustado pela inflação',
    'Gasto extra reinvestido (corrigido inflação)',
    'Soma rendimento + gastos evitados',
    'Inflação incidente sobre rendimento + gastos evitados',
    'Valor restante após dívida (2)',  # Renamed duplicate
    'Valorização do apartamento (inflação)',
    'Saldo acumulado',
    'Diferença'
]

# Fetch data using expected headers
data = sheet.get_all_records(expected_headers=expected_headers)

# Print the data
print(data)

