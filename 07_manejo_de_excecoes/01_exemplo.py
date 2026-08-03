#conversor de idade
print("========== CONVERSOR DE IDADE =========")
try:
    idade = int(input("Digite a sua idade: "))

    if idade < 0:
        print("A idade não pode ser negativa.")

    else:
        print(f"Você tem {idade} anos.")
        
except ValueError:
    print("Erro: você deve digitar apenas números.")

finally:
    print("Operação finalizada.")