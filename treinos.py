import os
os.system("cls")

"""
Arquivo pra treinar conceitos que ainda não domino muito 
Como no progra 1 - Que pratiquei, fazer calculos com valores de uma lista, append pra adicionar valor a uma lista, variável acumuladora e loop for e while
"""

# 1.0 Programa que multiplique todos os valores de uma lista
"""
numeros = [5, 5, 4]
multiplicadora = 1

for numero in numeros:
    multiplicadora *= numero

print(multiplicadora)
"""
# 1.1. Programa recebe vários números digitados pelo usuário e armazena-os em uma lista.
"""
numeros = []

escolha = 1

while escolha != 0:
    escolha = int(input("Digite um número (0 - sair): "))
    if escolha != 0:
        numeros.append(escolha)

print(numeros)
"""

# 1.2. Junção dos dois conhecimentos em um unico programa - Um programa que adiciona os números digitados numa lista (while / append) depois some os valores da lista (for)

numeros = []
numeros_escolhidos = 1
# Adicionar os números digitados pelo usuário na lista
while numeros_escolhidos != 0:
    numeros_escolhidos = int(input("Digite o número (0 - Sair): "))
    if numeros_escolhidos != 0:
        numeros.append(numeros_escolhidos)

# Percorrer cada número da lista e soma-los
soma = 0
for numero in numeros:
    soma += numero

print(f"""
    Lista........: {numeros}
    Lista somada.: {soma}
    """)



    
    