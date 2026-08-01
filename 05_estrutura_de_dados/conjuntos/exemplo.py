conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

união = conjunto1 | conjunto2
print("União:",união)

intersecao = conjunto1 & conjunto2
print("Interseção:", intersecao)

diferenca = conjunto1 - conjunto2
print("Diferença:", diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2
print("Diferença Simétrica:", diferenca_simetrica)

#métodos dos conjuntos
acessorios = {"Camisa", "Calça", "Meia", "Tênis", "Chapéu", "Mochila"}

acessorios.add("Cinto") #adicionando um item ao meu conjunto
print(acessorios)

acessorios.remove("Meia") #removendo um item do meu conjunto, se ele não existir, gera erro
print(acessorios)

acessorios.discard("Chapéu") #removendo um item do meu conjunto, caso ele exista. Se ele não existir, não faz nada
print(acessorios)

acessorios.clear() #limpando conjunto, removendo todos os itens, imprime set()
print(acessorios)