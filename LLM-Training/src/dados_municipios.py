import pandas as pd

# Caminho para o arquivo limpo
CAMINHO_ARQUIVO = "data/capag_municipios_limpo.csv"

# Carrega o CSV uma vez
df = pd.read_csv(CAMINHO_ARQUIVO)

#Função para buscar CAPAG dentro do arquivo CSV
def buscar_capag(municipio: str):
    # Normaliza a entrada (remove espaços extras e aplica título)
    municipios = [m.strip().title() for m in municipio.split("e")]

    resultados = []
    
    for m in municipios:
        # Normaliza o nome do município para comparação
        m = m.strip().title()

        # Refina a busca no dataframe para evitar confusão com substrings
        resultado = df[df["municipio"].str.contains(f"^{m}$", case=False, na=False)]

        if resultado.empty:
            resultados.append(f"Município '{m}' não encontrado. Verifique a digitação.")
        else:
            row = resultado.iloc[0]

            # Explicação das notas
            def explicacao_nota(nota):
                if nota == 'A':
                    return "Bom desempenho fiscal."
                elif nota == 'B':
                    return "Desempenho fiscal médio."
                elif nota == 'C':
                    return "Desempenho fiscal baixo."
                else:
                    return "Nota desconhecida."

            resultados.append(
                f"\nMunicípio: {row['municipio']} ({row['uf']})\n"
                f"CAPAG: {row['capag']}\n"
                f"Indicadores:\n"
                f"  - Endividamento: Nota {row['nota_1']} - {explicacao_nota(row['nota_1'])}\n"
                f"  - Poupança Corrente: Nota {row['nota_2']} - {explicacao_nota(row['nota_2'])}\n"
                f"  - Liquidez: Nota {row['nota_3']} - {explicacao_nota(row['nota_3'])}\n"
                f"ICF: {row['icf']}"
            )

    return "\n".join(resultados)


def comparar_municipios(municipio1: str, municipio2: str):
    # Normaliza o nome da cidade (tira espaços extras e aplica title case)
    municipio1 = municipio1.strip().title()
    municipio2 = municipio2.strip().title()
    
    # Busca nos dados
    resultado1 = df[df["municipio"].str.lower() == municipio1.lower()]
    resultado2 = df[df["municipio"].str.lower() == municipio2.lower()]

    if resultado1.empty or resultado2.empty:
        return f"Um ou ambos os municípios não foram encontrados. Verifique a digitação."

    row1 = resultado1.iloc[0]
    row2 = resultado2.iloc[0]

    # Explicação das notas
    def explicacao_nota(nota):
        if nota == 'A':
            return "Bom desempenho fiscal."
        elif nota == 'B':
            return "Desempenho fiscal médio."
        elif nota == 'C':
            return "Desempenho fiscal baixo."
        else:
            return "Nota desconhecida."

    return (
        f"Comparação entre {row1['municipio']} e {row2['municipio']}:\n\n"
        f"{row1['municipio']} ({row1['uf']}):\n"
        f"CAPAG: {row1['capag']}\n"
        f"  - Endividamento: Nota {row1['nota_1']} - {explicacao_nota(row1['nota_1'])}\n"
        f"  - Poupança Corrente: Nota {row1['nota_2']} - {explicacao_nota(row1['nota_2'])}\n"
        f"  - Liquidez: Nota {row1['nota_3']} - {explicacao_nota(row1['nota_3'])}\n"
        f"ICF: {row1['icf']}\n\n"
        
        f"{row2['municipio']} ({row2['uf']}):\n"
        f"CAPAG: {row2['capag']}\n"
        f"  - Endividamento: Nota {row2['nota_1']} - {explicacao_nota(row2['nota_1'])}\n"
        f"  - Poupança Corrente: Nota {row2['nota_2']} - {explicacao_nota(row2['nota_2'])}\n"
        f"  - Liquidez: Nota {row2['nota_3']} - {explicacao_nota(row2['nota_3'])}\n"
        f"ICF: {row2['icf']}"
    )
