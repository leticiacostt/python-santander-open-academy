print("========== DIÁRIO DE ESTUDOS ===========")

def adicionar_estudo():
    dia_estudado = input("Em qual dia da semana você estudou? ")
    horas_estudadas = input("Quantas horas você estudou? ")
    materia_estudada = input("Qual matéria você estudou hoje? ")
    assunto_estudado = input("Qual o assunto estudado? ")
    
    with open("08_leitura_e_escrita_de_arquivos/diario_estudos.txt", "a") as arquivo:
        arquivo.write(f"Dia Estudado: {dia_estudado} - Horas Estudadas: {horas_estudadas} - Matéria Estudada: {materia_estudada} - Assunto Estudado: {assunto_estudado}\n")
    
        print("Matéria adicionada!")

def ver_estudos():
    with open("08_leitura_e_escrita_de_arquivos/diario_estudos.txt", "r") as arquivo:
        conteudo = arquivo.read()
    
    print("\n========== MATÉRIAS ESTUDADAS ==========")
    print(conteudo)

def remover_estudos():
    dia_remover = input("Qual dia da semana você deseja remover? ")
    horas_remover = input("Qual carga horária você deseja remover? ")
    materia_remover = input("Qual matéria você deseja remover? ")
    assunto_remover = input("Qual assunto você deseja remover? ")
    
    with open("08_leitura_e_escrita_de_arquivos/diario_estudos.txt", "r") as arquivo:
        materias = arquivo.readlines()
    
    with open("08_leitura_e_escrita_de_arquivos/diario_estudos.txt", "w") as arquivo:
        for materia in materias:
            registro_remover = (f"Dia Estudado: {dia_remover} - Horas Estudadas: {horas_remover} - Matéria Estudada: {materia_remover} - Assunto Estudado: {assunto_remover}")
    
            if materia.strip() != registro_remover:
                arquivo.write(materia)
    
    print("Matéria removida!")

while True:
    print("\n1- Adicionar Matéria")
    print("2- Ver matérias")
    print("3- Remover matéria")
    print("4- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_estudo()

    elif opcao == "2":
        ver_estudos()

    elif opcao == "3":
        remover_estudos()

    elif opcao == "4":
        print("Encerrando o Diário de Estudos...")
        break

    else:
        print("Opção inválida! Escolha uma opção entre 1 e 4.")