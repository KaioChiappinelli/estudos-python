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
# Imprima os valores entre 1 e o valor digitado pelo usuário
"""
numero = int(input("Digite um número: "))
        # inicio   # fim   # passo
for i in range(1, numero + 1, 1):
    print(i)
"""

# Programa anterior 
"""
n = int(input("Tabuada de: "))
x = 1 
while x <= 10:
    print(n + x)
    x += n
"""
# Exercício 5.6 - Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada de multiplicação: 2x1 = 2, 2x2 = 4,...

numero = int(input("Início da tabuada: "))
x = 1

for x in range(numero, 20, 1):
    x = x + 1
    calculo = numero * x
    print(calculo)
    
    