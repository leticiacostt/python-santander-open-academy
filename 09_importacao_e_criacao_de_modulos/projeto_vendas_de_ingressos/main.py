from vendas import calcular_total
from recibo import gerar_recibo

VALOR_INGRESSO = 80
evento = "Show - Terno Rei"

nome= input("Digite seu nome: ")

try:
    quantidade = int(input("Quantidade de ingressos: "))

    total = calcular_total(quantidade, VALOR_INGRESSO)

    recibo = gerar_recibo(
        nome,
        evento,
        quantidade,
        total
    )

    print(recibo)

    with open("09_importacao_e_criacao_de_modulos/projeto_vendas_de_ingressos/recibo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(recibo)

    print("Recibo salvo com sucesso!")

except ValueError:
    print("Digite apenas números na quantidade de ingressos.")