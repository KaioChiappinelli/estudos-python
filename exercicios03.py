import os
os.system("cls")
'''
# Exercício 3.7 - pág 113

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

print(n1 + n2)

# Exercício 3.8 pág 113 - programa que leia o valor em metros exiba convertido em milímetros
print(50 * "=")
print(5 * " ", "Digite em metros e receba em milímetros\n")
valor = int(input("Digite um valor em metros: "))
conversao = valor * 1000

print(conversao)

# Exercício 3.9 pág 113 - Programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos.

quantidade_dias = float(input("Quantidade de dias: "))
quantidade_horas = float(input("Quantidade de horas: "))
quantidade_minutos = float(input("Quantidade de minutos: "))
quantidade_segundos = float(input("Quantidade de segundos: "))

total = (quantidade_dias * 86400) + (quantidade_horas * 3600) + (quantidade_minutos * 60) + quantidade_segundos

print(total)

# Exercício 3.10 - programa que calcule o aumento de salario. Ele solicita o valor do salario e a porcentagem do aumento. Exiba o valor do aumento do novo salário.

valor_salario = float(input("Digite o valor do salário: "))
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))

valor_aumento = valor_salario * porcentagem_aumento / 100
total_aumento = valor_salario + valor_aumento
print(f"O salario aumentou {porcentagem_aumento:2.0f}%, equivalente a R${valor_aumento:5.2f} e seu salário total foi de R${total_aumento:5.2f}")
'''
'''
# Exercício 3.11 - Faça um programa que que solicite o preço da mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar

# Solicitar preço e percentual
preco = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input('Digite o percentual de desconto (sem o "%"): '))

# Calculo da porcentagem
calc_desconto = preco * percentual_desconto / 100
valor_com_desconto = preco - calc_desconto

# Exibir valor do desconto e preço com desconto
print(f"\nVocê recebeu um desconto de {calc_desconto:.0f}%.\nTOTAL: R${valor_com_desconto:.2f}")

# Exercício 3.12 - Programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

# Solicitar distância a percorrer e velocidade média
distancia_a_percorrer = float(input('Digite a distância a percorrer em km: '))
velocidade_media = float(input('Digite a velocidade média da viagem em km/h: '))

tempo = distancia_a_percorrer / velocidade_media
print(tempo)
'''
'''
# Exercício 3.13 - Programa que converta uma temperatura digitada em graus celsios em fahrenheit.
print(51 * "=")
print(3 * "  ", "CONVERSÃO DE TEMPERATURA DE °C PARA °F")
print(51 * "=")

temperatura_em_celsios = int(input("Digite a temperatura em °C: "))

f = (9 * temperatura_em_celsios) // 5 + 32
print(f"\n{temperatura_em_celsios}°C é equivalente a {f}°F")

# Exercício 3.14 - Programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias que o carro foi alugado. Calcule o preço a pagar, sabendo que o aluguel custa R$60,00 por dia e R$0,15 por km rodado.

quilometros_percorridos = float(input("Quantidade km percorridos pelo carro alugado: "))
dias_com_carro = int(input("Quantidade de dias com o carro "))

preco_a_pagar = (quilometros_percorridos * 0.15) + (dias_com_carro * 60)

print(f"Dias percorridos -> {dias_com_carro}\nQuilometros percorridos -> {quilometros_percorridos}\nTOTAL A PAGAR: {preco_a_pagar}")
'''
# Exercício 3.15 - Programa que calcule a redução do tempo de vida de um fumante. Pergunte quantos cigarros ele fuma por dia e por quantos anos ele fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quanto tempo de vida ele perderá. Exiba o total em dias 

# Solicitar quantidade de cigarros por dia e quantos anos fuma
quantidade_cigarros_dia = int(input("Quantos cigarros por dia: "))
quantidade_anos_fuma = int(input("Quantos anos fumou: "))

total_de_cigarros = quantidade_cigarros_dia * (quantidade_anos_fuma * 365)
total_minutos_perdidos = total_de_cigarros * 10
total_dias_perdidos = total_minutos_perdidos // 1440

print(total_dias_perdidos)