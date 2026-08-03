#uso de args
def soma_variavel(*numeros): #traduzindo: receba quantos argumentos forem enviados e guarde tudo em uma tupla chamada numeros
    print(numeros)

soma_variavel(10, 20)
soma_variavel(10, 20, 30, 40)

def mostrar_materias(*materias):
    print(materias)

mostrar_materias(
    "Python",
    "IA",
    "Banco de Dados"
)

def mostrar_materias2(*materias):
    for materia in materias:
        print(materia)