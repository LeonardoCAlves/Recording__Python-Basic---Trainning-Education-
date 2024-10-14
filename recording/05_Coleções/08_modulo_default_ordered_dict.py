"""
Basicamente os valores dentro de um dicionário apesar de
apresentados na ordem de inserção, internamente esta ordem
não existe.
"""

from collections import OrderedDict, defaultdict
from datetime import datetime

# n1 = OrderedDict(
#     a=10, b=20
# )
#
# n2 = OrderedDict(
#     b=20, a=10
# )
#
# print(n1 == n2)

# Entregando tarefas:

while True:
    candidatos = []

    entregar = int(input('Tecle 1 para entregar ou 2 para sair: '))

    match entregar:
        case 1:
            quem = str(input('Quem está entregando: '))

            candidato = dict(
                nome=quem,
                tarefas=dict(
                    tarefa=str(input('Código da tarefa: ')),
                    dt=datetime.now().strftime('%d/%m/%Y %H:%M')
                )
            )

    candidatos.append(candidato)
    break


for dados in candidatos:
    for chave, valor in dados.items():
        if chave == 'nome':
            print(f'\n{chave}: {valor}')
        else:
            for c, v in valor.items():
                print(f'{c}: {v}', end=' | ')



