import os
os.system("cls")


def menu():
    print("""
            ===== CONTROLE DE SALDO =====

1 - Adicionar saldo
2 - Retirar saldo
3 - Consultar saldo
4 - Sair
""")

saldo_atual = 0
def adicionar_saldo(saldo_atual: float, saldo_adicionado: float) -> float:
    saldo_atual = saldo_atual + saldo_adicionado
    return saldo_atual

def retirar_saldo(saldo_atual: float, saldo_retirado: float) -> float:
    saldo_atual = saldo_atual - saldo_retirado
    return saldo_atual

def consultar_saldo(saldo_atual: float):
    print(f"Saldo atual: R$ {saldo_atual:.2f}")

def chamar_funcoes():
    menu()
    saldo_atual = 0
    opcao = 0
    while opcao != 4:
        opcao = int(input("\nEscolha: "))
        match opcao:
            case 1:
                adicionado = float(input("Quanto deseja adicionar: "))
                saldo_atual = adicionar_saldo(saldo_atual, adicionado)
                print(f"Saldo adicionado....: {adicionado}")
            case 2:
                retirado = float(input("Quanto deseja retirar: "))
                saldo_atual = retirar_saldo(saldo_atual, retirado)
                print(f"Saldo retirado....: {retirado}")
            case 3:
                consultar_saldo(saldo_atual)


chamar_funcoes()