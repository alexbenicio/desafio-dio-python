'''
DESAFIO DIO

Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
O sistema será desenvolvido para um banco que busca monetizar suas operações. 
Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python 
e criar um sistema funcional que simule as operações bancárias. 
Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

REGRAS
* LIMITE DE 3 SAQUES DIARIOS
* LIMITE DE R$ 500,00 POR SAQUE
* CONFIGURAR EXIBIÇÃO DOS NUMERÁRIOS DA SEGUINTE FORMA: R$ XXXX.XX
* NÃO É PERMITIDO DEPOSITO DE VALORES NEGATIVOS
* NÃO É PERMITIDO SAQUE COM VALOR SUPERIOR AO SALDO

'''

# Controles
VL_LIMITE_SAQUE = 500
QT_LIMITE_SAQUE = 3
SALDO_INICIAL = 0

# Variaveis
Saldo = 0
VlNumerario = 0
ContaCorrente = 0
Agencia = 1
numeroSaques = 0

# Métodos 

def saque():
    print("Iniciando operação de saque.")

def deposito():
    print("Iniciando operação de depósito")

def extrato():
    print("Aguarde a impressão do Extrato")

def menu():
    print("""
    *****************************
    *****************************
    Bem vindo ao Banco Digital AB
    -----------------------------
    Por favor, selecione a opção
    desejada:
    [S] - SAQUE
    [D] - DEPÓSITO
    [E] - EXTRATO
    [Q] - ENCERRAR A SESSÃO
    *****************************
    *****************************

    """)

def main():
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")
        opcao = opcao.upper()

        if opcao == 'S':
            saque()
        elif opcao == 'D':
            deposito()
        elif opcao == 'E':
            extrato()
        elif opcao == 'Q':
            print("Sessão encerrada.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Inicio da aplicacao
if __name__ == "__main__":
    main()
