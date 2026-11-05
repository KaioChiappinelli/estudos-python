import os
os.system("cls")

# Programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h exiba a mensagem "Você foi multado" e o valor da multa, cobrando 5 reais por km acima de 80 km/h

velocidade = float(input("Velocidade em km/h: "))

if velocidade > 80:
    velocidade_ultrapassada = velocidade - 80
    multa = velocidade_ultrapassada * 5
    print(f"Você foi multado em R${multa:.2f} por ultrapassar a velocidade permitida em {velocidade_ultrapassada:.2f} km/h!")
else: 
    if velocidade <= 0:
        print("Velocidade inválida, digite um número positivo!")
    else:
        if velocidade < 60:
            print("Muito abaixo do limite de velocidade, cuidado!")
        else:
            print("Velocidade adequada!")

# Programa que leia três números e imprima o maior e o menor 
'''
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))

if n1 > n2 and n1 > n3:
    print(f'O primeiro número "{n1}" é o maior número entre os três')
elif n2 > n1 and n2 > n3:
    print(f'O segundo número "{n2}" é o maior número entre os três')
elif n3 > n1 and n3 > n2:
    print(f'O terceiro número "{n3}" é o maior número entre os três')


if n1 < n2 and n1 < n3:
    print(f'O primeiro número "{n1}" é o menor número entre os três')
elif n2 < n1 and n2 < n3:
    print(f'O segundo número "{n2}" é o menor número entre os três')
else:
    print(f'O terceiro número "{n3}" é o menor número entre os três')
'''
# Programa que pergunte o salário do funcionário e e calcule o valor do aumento. Para salários superiores a R$1250,00 calcule um aumento de 10%. Para menor ou igual, de 15%
'''
print(50 * "=")
print(10 * " ", "PROGRAMA DE CALCULO DE AUMENTO")
print(50 * "=")
salario = float(input("Digite seu salário: "))

if salario > 1250:
    aumento = salario * 0.10
    total = salario + aumento
    print(f"Seu salário de R${salario:.2f} teve um aumento de 10% equivalente a R${aumento:.2f}\nTOTAL....................: R${total:.2f}")
elif salario <= 1250 and salario > 0:
    aumento = salario * 0.15
    total = salario + aumento
    print(f"Seu salário de R${salario:.2f} teve um aumento de 15% equivalente a R${aumento:.2f}\nTOTAL....................: R${total:.2f}")
'''
# Programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 k, e R$ 0,45 para viagens mais longas

distancia_desejada = float(input("Digite a distância que deseja percorrer em km: "))

if distancia_desejada <= 200:
    preco_passagem = distancia_desejada * 0.50 
    print(f"Você percorrerá uma distância de {distancia_desejada} pagando um valor de R$ 0,50 centavos por km.")
    print(50 * "-")
    print(f"TOTAL..............: R$ {preco_passagem:.2f}")
elif distancia_desejada > 200:
    preco_passagem = distancia_desejada * 0.45
    print(f"Você percorrerá uma distância de {distancia_desejada} pagando um valor de R$ 0,45 centavos por km.")
    print(50 * "-")
    print(f"TOTAL..............: R$ {preco_passagem:.2f}")
else:
    print("Digite apenas números positivos!")

