import random 
import os
os.system("cls")
'''
Módulo de repetições em python - Loop while e For
'''

# Programa que escreve a contagem regressiva de um foguete. O programa deve imprimir 10, 9, 8, 7..., 1, 0 e fogo! na tela.


"""
contagem = 10
while contagem > -1:
    print(contagem)
    contagem -= 1
print("Fogo!")
"""

# 1 - Crie um programa que:
# - Peça um número inteiro ao usuário.
# - Utilize um laço for para contar de 1 até esse número.
# - Mostre cada número na tela.



# Imprima os valores entre 1 e o valor digitado pelo usuário
'''
numero = int(input("Digite um número: "))
        # inicio   # fim   # passo
for i in range(1, numero + 1, 1):
'''

# Exercício 2 — Tabuada (Fácil/Intermediário)
# Crie um programa que:
# - Peça um número ao usuário.
# - Utilize um laço for.
# - Mostre a tabuada desse número de 1 até 10.

numero = int(input("Tabuada do: "))

for i in range(1, 10 + 1, 1):
    print(f"{numero} x {i} = {numero * i}")

# Exercício 3 - Adivinhe o número
# Crie um programa que:
# - Defina um número secreto (por exemplo, 8).
# - Peça ao usuário para tentar adivinhar.
# - Utilize um laço while para repetir enquanto ele não acertar.
# - Quando errar, informe que ele errou e peça novamente.
# - Quando acertar, mostre uma mensagem de parabéns.

print(50 * "=")
print(10 * " ", "ADIVINHE O NÚMERO")

tentativa = 0
numero_certo = random.randint(1, 10)

while tentativa != numero_certo:
    tentativa = int(input("Adivinhe o número: ")) 
    if tentativa != numero_certo:
        print("Tente novamente!")

print("Parabéns! Voce acertou!")