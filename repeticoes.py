import os
os.system("cls")

'''
Módulo de repetições em python - Loop while e For
'''

# Programa que escreve a contagem regressiva de um foguete. O programa deve imprimir 10, 9, 8, 7..., 1, 0 e fogo! na tela.

contagem = 10

while contagem > -1:
    print(contagem)
    contagem -= 1

print("Fogo!")

# Imprima os valores entre 1 e o valor digitado pelo usuário

numero = int(input("Digite um número: "))
        # inicio   # fim   # passo
for i in range(1, numero + 1, 1):
    print(i)
    
        
    
    