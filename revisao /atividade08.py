print("escolha seu personagem:")
print("1 - guerreiro")
print("2 - mago")
print("3 - arqueiro")

escolha = input("digite o nome ou numero da classe:")

if escolha == "1" or escolha == "guerreiro":
   print("vc escolheu guerreiro, prepare sua espada")
elif escolha == "2" or escolha == "mago":
   print("prepare a varinha para a magia")
elif escolha == "3"or escolha == "arqueiro":
   print("sua flecha derrubara os malfeitores")
else:
   print("opcao invalida,tente novamente")