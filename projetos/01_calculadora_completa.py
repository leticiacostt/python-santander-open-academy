#fazendo uma calculadora com entrada de dois números e vendo o resultado desse cálculo em cada uma das operações.
print("Inicializando a calculadora..."  )
number1 = float(input("Coloque o primeiro número: "))
number2 = float(input("Coloque o segundo número: "))

print("\n====== RESULTADOS ======")

soma = number1 + number2
print(f"A soma entre {number1} e {number2} é: {soma}.")

subtracao = number1 - number2
print(f"A subtração entre {number1} e {number2} é: {subtracao}.")

multiplicacao = number1 * number2
print(f"A multiplicação entre {number1} e {number2} é: {multiplicacao}.")

divisao = number1 / number2
print(f"A divisão entre {number1} e {number2} é: {divisao}.")

divisao_inteira = number1 // number2
print(f"A divisão inteira entre {number1} e {number2} é: {divisao_inteira}.")

modulo = number1 % number2
print(f"O módulo entre {number1} e {number2} é: {modulo}.")

exponenciacao = number1 ** number2
print(f"A exponenciação entre {number1} e {number2} é: {exponenciacao}.")

print("Finalizando a calculadora...")