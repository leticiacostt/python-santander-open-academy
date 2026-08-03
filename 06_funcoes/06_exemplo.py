#escopo de variáveis
def funcao():
    variavel_local = 10
    print(variavel_local)

funcao()
#print(variavel_local) ---> da erro

variavel_global = 20
def funcao2():
    print(variavel_global)

funcao2()