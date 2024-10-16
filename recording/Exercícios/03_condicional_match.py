valor = float(input('Digite o valor da transação: '))
tipo = int(input('Digite o tipo da transação [1] Débito [2] Crédito: '))

match tipo:
    case 1:
        if valor > 0:
            print(f'\nTransação: Débito | Valor: R${valor:.2f} | Status: Realizada.')
        else:
            print(f'\nTransação: Débito | Valor: Inválido | Status: NÃO Realizada.')
    case 2: 
        if valor > 0:
            print(f'\nTransação: Crédito | Valor: R${valor:.2f} | Status: Realizada.')
        else:
            print(f'\nTransação: Crédito | Valor: Inválido | Status: NÃO Realizada.')
    case _:
        print(f'\nOpção inválida!')