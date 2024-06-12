
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 16:
        print(f"{nome}, você está apto a emitir o seu título de eleitor pois tem {idade}.")
else:
    print(f"{nome}, você não está apto a emitir o seu título de eleitor pois tem somente {idade}.")
