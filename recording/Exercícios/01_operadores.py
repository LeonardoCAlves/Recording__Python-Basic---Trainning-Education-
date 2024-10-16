nome_produto = str(input('Nome do produto: '))
preco = float(input('Preço sem desconto: '))
desconto = float(input('Percentual de desconto (%): '))

# Forma 1
valor_desconto = preco * desconto/100
preco_com_desconto1 = preco - valor_desconto

# Forma 2
preco_com_desconto2 = preco - preco * desconto/100

# Forma 3
preco_com_desconto3 = preco * (1 - desconto/100)

print('\n\nResumo do Produto:')
print(f'Nome: {nome_produto}')
print(f'Preço com desconto: R$ {preco_com_desconto1:.2f}')
print(f'Preço com desconto: R$ {preco_com_desconto2:.2f}')
print(f'Preço com desconto: R$ {preco_com_desconto3:.2f}')