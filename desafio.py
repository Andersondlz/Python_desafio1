menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0 
LIMITE_SAQUES = 3

while True:

    opcao =  input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Informe o valor do Deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print("Valor não poderá ser negativo")

    elif opcao == "s":
        print("Saque")
        if numero_saque < LIMITE_SAQUES:
            saque = float(input("Informe o valor do Saque: "))
            if saque <= limite and saque <= saldo:
                saldo -= saque  
                numero_saque += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
            elif saque > limite:
                print("Seu limite de Saque tem que ser abaixo de R$ 500,00")
            else:
                print("Saldo Indisponivel para operação")
        else:
            print("Você já estourou o limite de SAQUE DIARIO")

    elif opcao == "e":
        print("\n=============Extrato================")
        print("Não foram realizados movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("====================================")

    
    elif opcao == "q":
        break

    else:
        print("Operaçao invalida, por favor selecione novamente a operaçao desejada.")
    