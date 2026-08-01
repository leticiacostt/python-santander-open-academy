print("Invocando o Chapéu Seletor...")
print("Olá, caro Aluno(a)...")

grifinoria = 0
corvinal = 0
sonserina = 0
lufalufa = 0

print("Qual característica combina mais com você?")
print("1- Coragem")
print("2- Inteligência")
print("3- Ambição")
print("4- Lealdade")
pergunta1 = input("Escolha uma opção: ")

if pergunta1 == "1":
    grifinoria += 1
elif pergunta1== "2":
    corvinal += 1
elif pergunta1== "3":
    sonserina += 1
elif pergunta1== "4":
    lufalufa += 1

print("Em um trabalho você costuma: ")
print("1- Liderar")
print("2- Pesquisar e Planejar")
print("3- Buscar o melhor resultado")
print("4- Ajudar todos")
pergunta2 = input("Escolha uma opção: ")

if pergunta2== "1":
    grifinoria += 1
elif pergunta2 == "2":
    corvinal += 1
elif pergunta2== "3":
    sonserina += 1
elif pergunta2== "4":
    lufalufa += 1

print("O que mais você valoriza? ")
print("1- Honra")
print("2- Conhecimento")
print("3- Poder")
print("4- Amizade")
pergunta3 = input("Escolha uma opção: ")

if pergunta3== "1":
    grifinoria += 1
elif pergunta3=="2":
    corvinal += 1
elif pergunta3 == "3":
    sonserina += 1
elif pergunta3== "4":
    lufalufa += 1

print("Se encontrasse um desafio, você: ")
print("1- Enfrentaria imediatamente")
print("2- Estudaria a situação")
print("3- Procuraria uma vantagem estratégica")
print("4- Pediria ajuda à equipe")
pergunta4 = input("Escolha uma opção: ")

if pergunta4== "1":
    grifinoria += 1
elif pergunta4== "2":
    corvinal += 1
elif pergunta4== "3":
    sonserina += 1
elif pergunta4 == "4":
    lufalufa += 1

if grifinoria > corvinal and grifinoria > sonserina and grifinoria > lufalufa:
    print("Você pertence à Grifinória!")
elif corvinal > grifinoria and corvinal > sonserina and corvinal> lufalufa:
    print("Você pertence à Corvinal!")
elif sonserina > grifinoria and sonserina > corvinal and sonserina > lufalufa:
    print("Você pertence à Sonserina!")
elif lufalufa > grifinoria and lufalufa > corvinal and lufalufa > sonserina:
    print("Você pertence à LufaLufa!")
else:
    print("O chapéu Seletor detectou um empate!")

print("\n ===== RESULTADO =====")
print("Grifinoria:", grifinoria)
print("Corvinal:", corvinal)
print("Sonserina:", sonserina)
print("Lufa-Lufa:", lufalufa)