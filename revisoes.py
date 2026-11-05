import os
os.system("cls")

"""
    Arquivo para realizar revisões de conteúdos passados do livro
"""

# Revisão com exercícios - Condições

# Programa que leia três números e exiba o maior 

print(100 * "=")
print(25 * " ", "Digite 3 números e o programa exibirá o maior entre eles")
print(100 * "=")

def calcula_numero_maior(num1: int, num2: int, num3: int):
    if num1 > num2 and num1 > num3:
        print(f"O maior número entre os três digitados é o {num1}!")
    elif num2 > num1 and num2 > num3:
        print(f"O maior número entre os três digitados é o {num2}!")
    else:
        print(f"O maior número entre os três digitados é o {num3}!")

num1_digitado = int(input("Número 1: "))
num2_digitado = int(input("Número 2: "))
num3_digitado = int(input("Número 3: "))
calcula_numero_maior(num1_digitado, num2_digitado, num3_digitado)

# Programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250, calcule um aumento 10%. Para inferiores ou iguais, um aumento de 15%

print(130 * "=")
print("Programa que calcula aumento de salário -> superiores a R$ 1.250, um aumento 10%. Para inferiores ou iguais, um aumento de 15%")
print(130 * "=")


salario = float(input("Digite o salário: "))
if salario <= 1250:
    aumento = salario * 0.15
    total = salario + aumento
    print(f"SALÁRIO.........: {salario:.2f}")
    print(f"AUMENTO.........: {aumento:.2f}")
    print(f"TOTAL...........: {total:.2f}")
elif salario > 1250:
    aumento = salario * 0.10
    total = salario + aumento
    print(f"SALÁRIO.........: {salario:.2f}")
    print(f"AUMENTO.........: {aumento:.2f}")
    print(f"TOTAL...........: {total:.2f}")
else:
    print("Inválido")