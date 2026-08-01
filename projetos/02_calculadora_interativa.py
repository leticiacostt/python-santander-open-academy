#preciso mostra um menu, pedir ao usuário para escolher uma operação, pedir os números, executar apenas a operação escolhida usando if, elif e else.
print("Inicializando a calculadora interativa...")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Qual operação você deseja executar? ")

if operacao not in ["1", "2", "3", "4"]:
    print("Operação inválida. Por favor, escolha outra opção.")
else:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        soma = numero1 + numero2
        print(f"A soma entre {numero1} e {numero2} é: {soma}")
    elif operacao == "2":
        subtracao = numero1 - numero2
        print(f"A subtração entre {numero1} e {numero2} é: {subtracao}")
    elif operacao == "3":
        multiplicacao = numero1 * numero2 
        print(f"A multiplicação entre {numero1} e {numero2} é: {multiplicacao}")
    elif operacao == "4":
        if numero2 == 0:
            print("Divisão por 0 não é permitida.")
        else:
            divisao = numero1 / numero2
            print(f"A divisão entre {numero1} e {numero2} é: {divisao}")

