"""
Booleano >>> 2 constantes - Verdadeiro e falso.

Maneira direta de testar booleano >>>  print('a' in 'maria')
"""

usuario = False  # usuario ainda não pg
status = usuario

res = input('Se a conta foi paga? [S para sim | N para não]: ').lower()

if res == 's':
    status = not usuario

print(status)