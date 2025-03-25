import pandas as pd

# Caminho do seu arquivo .xlsx original
caminho_excel = "C:/Users/Victor Bellé/Desktop/Projetos Python/LLM-Training/data/CAPAG-Municipios-posicao-2025-fev-19.xlsx"

# Carrega a planilha
df = pd.read_excel(caminho_excel, engine="openpyxl")

# Converte para CSV
caminho_csv = "data/capag_municipios.csv"
df.to_csv(caminho_csv, index=False)

print(f"Arquivo convertido com sucesso: {caminho_csv}")