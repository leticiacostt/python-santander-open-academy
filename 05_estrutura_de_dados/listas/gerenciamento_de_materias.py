print("===== MATÉRIAS DO SEMESTRE =====")
materias_do_semestre = [] #criando a lista

for i in range (6): #pedindo pra ser executado 6 vezes
    materia = input("Qual matéria você deseja adicionar? ")
    materias_do_semestre.append(materia)

print("Materias Cadastradas: ")

for materia in materias_do_semestre: #vai pegar cada item dentro da lista
    print(materia)
    
while True:
    resposta1 = input("Deseja remover a primeira matéria da lista? (S/N) ").upper()

    if resposta1 == "S":
        materias_do_semestre.pop(0) #remove a primeira matéria da lista, por índice
        break

    elif resposta1 == "N":
        print("Ok, a primeira matéria não será removida da lista.")
        break

    else:
        print("Opção inválida. Por favor, digite 'S' para sim ou 'N'para não.")


while True:
    resposta2 = input("Deseja ordenar a lista de matérias em ordem alfabética? (S/N) ").upper()

    if resposta2 == "S":
        materias_do_semestre.sort() #ordena a lista em ordem alfabética
        break

    elif resposta2 == "N":
        print("Ok, a lista não será ordenada.")
        break

    else:
        print("Opção inválida. Por favor, digite 'S' para sim ou 'N'para não.")

while True:
    resposta3 = input("Deseja inverter a ordem da lista de matérias? (S/N) ").upper()
    if resposta3 == "S":
        materias_do_semestre.reverse() #inverte a ordem da lista
        break

    elif resposta3 == "N":
        print("Ok, a lista não será invertida.")
        break

    else:
        print("Opção inválida. Por favor, digite 'S' para sim ou 'N'para não.")


while True:
    resposta4 = input("Deseja remover alguma outra matéria da grade? (S/N)").upper() #qual matéria remover da lista de acordo com o o que o usário digitar
    if resposta4 == "S":
        materia_remover = input("Qual matéria você deseja remover? ")

        if materia_remover in materias_do_semestre:
            materias_do_semestre.remove(materia_remover)
            print("Matéria removida com sucesso!")
            break
        else:
            print("Matéria não cadastrada na grade. Por favor, verifique o nome da matéria e tente novamente.")

    elif resposta4 == "N":
        print("Ok, nenhuma matéria será removida da lista.")
        break

    else:
        print("Opção inválida. Por favor, digite 'S' para sim ou 'N'para não.")

print("ATUALIZANDO SUA LISTA DE MATÉRIAS DO SEMESTRE...")
print("Grade de matérias atualizada: ") #atualização da lista de matérias do semestre
for materia in materias_do_semestre:
    print(materia)