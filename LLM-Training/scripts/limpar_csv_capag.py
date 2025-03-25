import pandas as pd

input_path = "data/capag_municipios.csv"
output_path = "data/capag_municipios_limpo.csv"

# Carrega o CSV corretamente, pulando as duas primeiras linhas
df = pd.read_csv(input_path, skiprows=2, sep=",", encoding="utf-8")

# Renomeia as colunas principais
df.rename(columns={
    "Nome_Município": "municipio",
    "UF": "uf",
    "CAPAG": "capag",
    "Indicador 1": "indicador_1",
    "Nota 1": "nota_1",
    "Indicador 2": "indicador_2",
    "Nota 2": "nota_2",
    "Indicador 3": "indicador_3",
    "Nota 3": "nota_3",
    "ICF": "icf"
}, inplace=True)

# Seleciona apenas as colunas úteis
colunas_utilizadas = [
    "municipio", "uf", "capag",
    "indicador_1", "nota_1",
    "indicador_2", "nota_2",
    "indicador_3", "nota_3",
    "icf"
]

df_limpo = df[colunas_utilizadas].copy()

# Remove linhas sem município ou sem CAPAG
df_limpo.dropna(subset=["municipio", "capag"], inplace=True)

# Salva o novo arquivo limpo
df_limpo.to_csv(output_path, index=False)

print(f"✅ CSV limpo salvo com sucesso em: {output_path}")
