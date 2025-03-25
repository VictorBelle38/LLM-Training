from src.dados_municipios import buscar_capag

while True:
    user_input = input("Você: ")
    
    if user_input.lower() in ["sair", "exit"]:
        break

    # Exemplo simples de verificação de intenção
    if "capag" in user_input.lower():
        cidade = user_input.split("de")[-1].strip()
        resposta = buscar_capag(cidade)
    else:
        resposta = "Ainda estou aprendendo sobre isso!"

    print("BotSquad:", resposta)