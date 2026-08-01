print("====== NOTAS ======")
nota = float(input("Informe sua nota: "))

situacao = ""

if nota < 0 or nota > 10:
    situacao = "Nota inválida! Por favor, insira uma nota entre 0 e 10!" #classificando se a nota existe dentro da faixa permitida
elif nota >= 9:
    situacao = "Sua nota foi excelente!"
elif 7 <= nota <= 8.9:
    situacao = "Aluno aprovado!"
elif 5 <= nota <= 6.9:
    situacao = "Você está de recuperação!"
else:
    situacao = "Aluno reprovado!"
print(situacao)