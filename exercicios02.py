import os
os.system("cls")

# Exercicio 3.4 pág 100
# Escreva uma expressão para determinar se o usuario deve ou não pagar imposto. Pagam impostos pessoas cujo o salario é maior que R$ 1.200,00

nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))

if idade < 18:
    print(30 * "-")
    print(f"Idade: {idade}\nMenor de idade. SAIA!")
else:
    if salario > 1200:
        print(30 * "-")
        print(f"Salário = {salario}\nVocê deve pagar impostos!")
    else:
        print(f"Salário = {salario}\nVocê não paga impostos!")

# Exercício 3.6 pág 100
# Escreva uma expressão qçue será utilizada para decidir se um aluno foi ou não aprovado para ser aprovado todas as médias do aluno deve ser maior ou igual a 7. Considre que o aluno cursa 3 matérias.
print(30 * "-")
print(" - EXERCÍCIO 3.6 -")
print(30 * "-")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media_materia1 = (nota1 + nota2) / 2
print(f"\nMédia disciplina 1 -> {media_materia1}")

nota3 = float(input("Nota 1: "))
nota4 = float(input("Nota 2: "))
media_materia2 = (nota1 + nota2) / 2
print(f"\nMédia disciplina 2 -> {media_materia2}")

nota5 = float(input("Nota 1: "))
nota6 = float(input("Nota 2: "))
media_materia3 = (nota1 + nota2) / 2
print(f"\nMédia disciplina 3 -> {media_materia3}")

if media_materia1 and media_materia2 and media_materia3 > 7:
    print("Aprovado!")
else:
    print("Reprovado!")







