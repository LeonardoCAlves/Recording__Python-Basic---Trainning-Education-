import datetime

saldo = 1000
contador_retiradas = 1

while True:
    opcao = int(input("\n===== CAIXA ELETRÔNICO =====\n \
    1. Sacar\n2. Visualizar Saldo e Retiradas\n3. Sair\n \
    Digite o número da opção desejada: "))

    if opcao == 1:
        valor_saque = float(input("\nDigite o valor que deseja sacar: "))

        if valor_saque > saldo:
            print("\nSaldo insuficiente. Operação não realizada.")
        else:
            saldo -= valor_saque
            data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            nome_variavel = f"retirada_{contador_retiradas}_{data_hora}"
            globals()[nome_variavel] = valor_saque  
            contador_retiradas += 1
            print(f"\nSaque de R${valor_saque:.2f} realizado com sucesso.")
            print(f"Saldo restante: R${saldo:.2f}")

    elif opcao == '2':
        print(f"\n\nSaldo atual: R${saldo:.2f}")
        retirada_vars = [var_name for var_name in globals() if var_name.startswith('retirada_')]
        print("\nHistórico de Retiradas:")
        for var_name in retirada_vars:
            var_value = globals()[var_name]
            print(f"{var_name}: R${var_value:.2f}")

    elif opcao == '3':
        print("\nEncerrando o caixa eletrônico.\n\n")
        break
    else:
        print("\nOpção inválida. Por favor, digite 1, 2 ou 3.")