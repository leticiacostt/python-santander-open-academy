#try, except, finally
print("========== BANCO PYTHON ==========")

#criando um exececao personalizada
class SaldoInsuficienteError(Exception):
    pass #significa não faça nada aqui por enquanto, instrução vazia pois o python não permite deixar um bloco sem código

def sacar(valor, saldo):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")

    return saldo - valor

saldo_atual = 100

try:
    valor_saque = ( int(input("Digite o valor que você deseja sacar: ")))

    novo_saldo = sacar(valor_saque, saldo_atual)

    print("Saque realizado com sucesso.")
    print(f"Seu novo saldo é de {novo_saldo}")

except ValueError:
    print("Erro: digite apenas números.")

except SaldoInsuficienteError as erro:
    print(f"Não foi possível realizaro saque: {erro}.")

finally:
    print("Encerrando atendimento.")