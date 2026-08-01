for numero in range(1, 11):
    if numero == 5:
        break
    print(numero)

while True:
    senha = input("Digite sua senha: ")

    if senha == "Bemfacil123":
        print("Acesso permitido!")
        break
    print("Senha incorreta!")