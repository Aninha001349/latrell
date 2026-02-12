try:
    energia = int(input("digite o nivelde energia do jogador(0-100): "))
    if energia >= 70:
        classificaçao = "alta"
    elif 30 <= energia <=69:
        classificaçao = "media"
    elif energia >= 0:
        classificaçao = "baixa"
    else:
        classificaçao = "valor invalido (negativo)"

    print(f"status do jogador {classificaçao}")
except ValueError:
    print("por favor,digite apenas numeros inteiros.") 