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

class ContaUnica:
    def __init__(self, vl_limite_saque, qt_limite_saque, saldo, numero_saques, extrato_detalhe):
        self.vl_limite_saque = vl_limite_saque
        self.qt_limite_saque = qt_limite_saque
        self.saldo = saldo
        self.numero_saques = numero_saques
        self.extrato_detalhe = extrato_detalhe
    # Métodos 
    def saque(self):
        vl_numerario = float(input(("Informe o valor do saque: ")))
        if self.numero_saques < self.qt_limite_saque:
            if vl_numerario <= self.vl_limite_saque:
                if vl_numerario <= self.saldo:
                    self.saldo -= vl_numerario
                    self.extrato_detalhe += f"\n    Saque: R$ {vl_numerario:.2f}\n"
                    print("Saque realizado com sucesso!")

                    # Incremento de quantidade de saques realizados
                    self.numero_saques += 1
                else:
                    print("""
    Falha na operação. 
    Motivo:  Saldo insuficiente. Por 
    favor, tente novamente com outro
    valor. 
                    """)
        
            else:
                print("""
    Falha na operação. 
    Motivo:  Valor máximo para saque 
    é de R$ 500,00 por operação. Por 
    favor, tente novamente com outro
    valor. 
                """)

        else:
            print("""\n
    Falha na operação. 
    Motivo: Você já esgotou o total 
    de  3 saques autorizados para o 
    dia de hoje. 
    Tente novamente amanhã.
            """)

    def deposito(self):
        vl_numerario = float(input(("Informe o valor do depósito: ")))

        if vl_numerario > 0:
            self.saldo += vl_numerario
            self.extrato_detalhe += f"\n    Depósito: R$ {vl_numerario:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
                        print("""\n
    Falha na operação. 
    Motivo: Valor de depósito inválido.
                        """)

    def extrato(self):
        print(f"""
    *****************************
    *****************************
        Banco Digital AB
    -----------------------------
            EXTRATO
    {self.extrato_detalhe}

    SALDO ATUAL: {self.saldo}
    *****************************
    *****************************

        """)

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
    #Configurando conta única
    # Controles
    VL_LIMITE_SAQUE = 500
    QT_LIMITE_SAQUE = 3
    SALDO = 0

    # Variaveis
    numero_saques = 0
    extrato_detalhe = """
    -----------------------------
    """
    conta = ContaUnica(VL_LIMITE_SAQUE,
                       QT_LIMITE_SAQUE,
                       SALDO,
                       numero_saques,
                       extrato_detalhe)
    while True:
        menu()
        opcao = input("Digite a opção desejada: ")
        opcao = opcao.upper()

        if opcao == 'S':
            conta.saque()
        elif opcao == 'D':
            conta.deposito()
        elif opcao == 'E':
            conta.extrato()
        elif opcao == 'Q':
            print("Sessão encerrada.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Inicio da aplicacao
if __name__ == "__main__":
    main()
