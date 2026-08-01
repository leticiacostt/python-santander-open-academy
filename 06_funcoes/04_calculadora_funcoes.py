
def somar(numero1, numero2): #recebe dois números e retorna a soma deles
    return numero1 + numero2

def subtrair(numero1, numero2): #recebe dois números e retorna a diferença entre eles
    return numero1 - numero2

def multiplicar(numero1, numero2): #recebe dois números e retorna a multiplicação deles
    return numero1 * numero2

def dividir(numero1, numero2): #recebe dois números e retorna a divisão deles
    if numero2 == 0:
        return None

    return numero1 / numero2

continuar = True

while continuar:

    print("========== CALCULADORA ===========")

    print("""
    Escolha uma operação:
    1- Soma
    2- Subtração
    3- Multiplicação
    4- Divisão
    5- Sair
    """)

    opcao= int(input("Digite a operação desejada: "))

    if opcao == 5:
        continuar = False
        print("Encerrando calculadora...")

    else:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: ")) 
        
        if opcao == 1:
            resultado = somar(numero1, numero2)
            print(resultado)

        elif opcao == 2:
            resultado = subtrair(numero1, numero2)
            print(resultado)

        elif opcao == 3:
            resultado = multiplicar(numero1, numero2)
            print(resultado)

        elif opcao == 4:
            resultado = dividir(numero1, numero2)

            if resultado is None:
                print("Não é possível dividir por zero.")
            else:
                print(resultado)   