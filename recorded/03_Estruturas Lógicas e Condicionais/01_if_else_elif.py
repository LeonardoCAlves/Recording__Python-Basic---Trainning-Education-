"""
IF, ELSE, ELIF
Estrutura condicional.
Permite que o código siga por caminhos diferentes de acordo com as decisões que são tomadas.

Vale ressaltar que ELIF só existe em PYTHON
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''

media = float(input('Digite a nota: '))

# Condição simples
if media >= 7.0:
    print('Aluno foi APROVADO!')
else:
    print('Aluno foi REPROVADO!')


# Condição composta
if (media >= 7.0) and (media <= 10.0):
    print('Aluno foi APROVADO.')

elif (media < 7.0) and (media >= 5):
    print('Aluno em RECUPERAÇÃO.')

elif (media < 5.0) and (media >= 0):
    print('Aluno foi REPROVADO.')

else:
    print('Algo errado não está certo!')

################################################################

''' Vamos criar um sistema para validadar se o cliente
pode ou não ter uma Habilitação de acordo com a idade 
que irá informar.
'''

# Condição aninhada
idade = int(input('idade: '))

if (idade >= 18) and (idade <= 65):
    print('Você pode tirar sua CNH...')

elif (idade >= 16) and (idade < 18):
    auto = str(input('Você tem Autorização? [S | N]: ')).upper()
    if auto == 'S':
        print('Ok, vamos continuar...')
    
    elif auto == 'N':
        print('Ops, não podemos continuar...')

    else:
        print('Resposta inválida!')

else:
    print('Você NÃO pode tirar sua CNH...')

################################################################

# Operadores unitários >>> Dependem de um único valor >>> not, is
# Operadores binários >>> Dependem de mais que 1 valor >>> and, or

numero = 10

if numero > 5:
    print('ok')

if not numero > 5:
    print('ok')

if (numero >= 5) and (numero <= 10):
    print('ok')

if (numero >= 5) or (numero <= 10):
    print('ok')
