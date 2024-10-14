"""
Print >>> Função interna com a finalinadede mostrar um 
          valor na tela.
Input >>> Função interna com a finalidade de solicitar 
          que o usuário insira um determinado dado.
"""

nome = 'Leonardo'
print(nome)

idade = int(input('Idade: '))
print(nome, idade)

# print formatado (Menos usual)
print('Oi ' + nome + ', legal saber que vc tem', idade, 'anos de idade.')
print('Oi {}, legal saber que vc tem {} anos de idade.'.format(nome, idade))

# Fstring (Mais usual)
print(f'Oi {nome}, legal saber que vc tem {idade} anos de idade.')

