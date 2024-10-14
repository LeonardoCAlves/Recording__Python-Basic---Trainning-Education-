"""
Default Dict permite criar uma dicionário passando um valor default
para chaves antes da inserção dos valores e/ou até mesmo quando o valor
não será passado. Caso tentemos acessar uma chave que não existe, essa
chave será criada com valor default que configuramos.
"""

from collections import defaultdict

dados = defaultdict(lambda: 'valor temporário')

dados['nome'] = 'Leonardo'

print(dados['idade']) # em um dic normal, teríamos um keyerror

print(dados)