"""
ESTRUTURA DE REPETIÇÃO

For >>> Utilizada quando se sabe a quantidade de repetições que serão necessárias,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe >>> for item in iteravel:
                execução

* Range
    Ex. Contador 10 - 0
                 0 - 10
                  step

* Enumerate
     Ex. for valor in enumerate(frase)

* String (palavra, frase)
* Lista

"""

# for item in iterável:
#     conteúdo que será repetido

# for cont in range(0, 11, 1):   De 0 a 10 indo de 1 em 1
# for cont in range(11):         De 0 a 10 indo de 1 em 1
# for cont in range(0, 11, 2):   De 0 a 10 indo de 2 em 2
# for cont in range(10, -1, -1): De 10 a 0 indo de -1 em -1


soma = 0
for contador in range(4):
    print('soma', soma)
    nota = float(input(f'{contador + 1}1 nota:'))
    soma += nota

print(f'Média: { soma}')   