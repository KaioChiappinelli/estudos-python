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
"""
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

print(f
    # Lista........: {numeros}
    # Lista somada.: {soma}
    )
numeros = []
numeros_escolhidos = 1
"""

'''
# Ex 1.

pontos = 0

pontos += 10
pontos += 20
pontos -= 5
print(pontos)

# Ex 2.

numero = 10
numero = numero * 2
numero = numero + 15
numero = numero / 5
print(numero)

# Ex 3.

saldo = 0

while saldo < 40:
    saldo = saldo + 10
    print(saldo)

# Ex 4.
total = 0
entrada = " "
while entrada != "s":
    entrada = input("Digite um número (s - sair): ")
    if entrada != "s":
        numero_convertido = float(entrada)
        total += numero_convertido

print(f"Total acumulado: {total}")
'''        

# Ex 5.
'''
nota = None

if nota is None:
    print("Nenhuma nota cadastrada!")
    nota = float(input("Digite a nota: "))
    print(f"Nota cadastrada..: {nota}")

# Ex 6.
def calcular_desconto(preco: float, desconto: float) -> float:
    resultado = preco - (preco * desconto)
    return resultado

preco_digitado = float(input("Digite o preço: "))
desconto_digitado = float(input("Digite o desconto: "))
desconto_decimal = desconto_digitado / 100


total = calcular_desconto(preco_digitado, desconto_decimal)
print(total)

# Ex 7.
def saudacao(nome: str, mensagem = "Bom dia") -> str:
    mn = mensagem + "," + " " + nome + "!"
    return mn

mensagem = saudacao("Flávio")
print(mensagem)
'''
# Ex 8 - Final 
"""Crie uma função chamada mostrar_resultado().

Ela deverá:
1. Receber um parâmetro chamado resultado.
2. O parâmetro deverá ter None como valor padrão.
3. Se o resultado for None, retornar "Nenhum cálculo realizado.".
4. Caso contrário, retornar "Último resultado: X", substituindo X pelo valor recebido."""

def mostrar_resultado(resultado = None):
    if resultado is None:
        return "Nenhum cálculo realizado."
    else:
        resultado = f"Último resultado: {resultado}"
        return resultado

print(mostrar_resultado())
print(mostrar_resultado(250))