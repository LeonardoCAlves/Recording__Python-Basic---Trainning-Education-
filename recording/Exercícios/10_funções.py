def calcular_gorjeta(valor_conta, bebida_especial, tempo):
    gorjeta = valor_conta * 0.10

    if bebida_especial.lower() == 'sim':gorjeta += 5.00

    horas, minutos = map(int, tempo.split(':'))
    if horas > 1 or (horas == 1 and minutos > 30):gorjeta += 15.00

    return gorjeta

total_gorjetas = 0
while True:
    valor_conta = float(input("\nDigite o valor da conta: R$ "))
    bebida_especial = input("Houve bebida especial? (sim/não): ")
    tempo = input("Digite o tempo de permanência (hh:mm): ")

    gorjeta = calcular_gorjeta(valor_conta, bebida_especial, tempo)
    total_gorjetas += gorjeta

    print(f"\nO valor da gorjeta para esta mesa é: R$ {gorjeta:.2f}")
    
    while True:
        continuar = input("\nDeseja inserir outra mesa? (s/n): ").strip().lower()
        if continuar == 'n':
            break
        elif continuar == 's':
            break
        else:
            print('Opção inválida!')

    if continuar == 'n': break
    
print(f"\n\nSuas gorjetas hoje: R$ {total_gorjetas:.2f}")