import datetime

nome = input("Digite o nome do cliente: ")
data_nascimento = input("Digite a data de nascimento (no formato DD/MM/AAAA): ")

data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
data_atual = datetime.datetime.now()
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

if idade <= 12:status = "Ops, não podemos prosseguir!"
elif idade <= 17:
    if idade <= 15:status = "Ops, não podemos prosseguir..."
    elif idade <= 17:
        autorizacao = input("Tem autorização dos responsáveis? (sim/não): ").lower()
        if autorizacao == "sim":status = "Ok, vamos prosseguir..."
        else:status = "Ops, não podemos prosseguir..."
elif idade <= 64:status = "Ok, vamos prosseguir..."
else:
    autorizacao_medica = input("Tem autorização médica? (sim/não): ").lower()
    if autorizacao_medica == "sim":status = "Ok, vamos prosseguir..."
    else:status = "Ops, não podemos prosseguir..."


print(f"Informações para {nome}: {status}")