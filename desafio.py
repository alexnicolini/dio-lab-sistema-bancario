# Declara variáveis globais do sistema
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    # Verifica qual operação o usuário deseja realizar
    if opcao == "d": # DEPÓSITO
        valor = float(input("Informe o valor do depósito: "))

        # Verifica se o valor do depósito é um valor válido (positivo)
        if valor > 0: 
            saldo += valor # deposita na conta
            extrato += f"Depósito: R$ {valor: .2f}\n" # registra histórico de depósitos
            print(extrato)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":  # SAQUE
        valor = float(input("Informe o valor do saque: "))

        # Realiza verificações
        # 1. Verifica se possui saldo suficiente para realizar o saque
        excedeu_saldo = valor > saldo 
        # 2. Verifica se o limite máximo para saque foi excedido
        excedeu_limite = valor > limite
        # 3. Vefica se já atingiu a quantidade máxima de saques diários
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operaçõu falhou! Número máximo de saques excedido.")

        # Verifica se está sacando um valor negativo na conta
        elif valor > 0:
            saldo -= valor # debita da conta
            extrato += f"Saque: R$ {valor:.2f}\n" # registra histórico de saques
            numero_saques += 1 # atualiza a quantidade de saques diário
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e": # EXTRATO
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q": # SAIR DO SISTEMA
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")
