"""
Importado da biblioteca Collections

Counter recebe um iterável como parâmetro e cria um objeto do tipo
Collections Counter (parecido com um dicionário), sendo a chave o
elemento da lista e o valor a quantidade de vezes que este valor
se repete.
"""

from collections import Counter
import re


# frutas = [
#     'uva', 'pera', 'uva', 'goiaba', 'uva', 'pera', 'uva', 'uva',
#     'uva', 'uva', 'goiaba', 'melão', 'mamão', 'laranja', 'maçã',
#     'pera', 'goiaba', 'pera', 'pera', 'mamão', 'pera', 'pera'
# ]
#
# cont = Counter(frutas)
#
# for c, v in cont.items():
#     print(f'{c} => {v}')


# exemplo 2 ===================================================

texto = 'Na parte 1, explico como cada um de nós está condicionado a ' \
        'pensar e agir nos assuntos financeiros e esboço quatro estratégias chave' \
        'para você rever o seu modelo mental de dinheiro. Na parte 2, examino ' \
        'as diferenças entre o modo de pensar das pessoas ricas e da grande' \
        'maioria das pessoas. Além disso, sugiro 17 atitudes e ações capazes ' \
        'de promover mudanças permanentes na sua vida financeira. E qual é a minha experiência? ' \
        'De onde venho? Sempre fui bem sucedido? Quem dera!' \
        'Assim como um grande número de pessoas, sempre tive muito ' \
        'potencial, mas os resultados que conseguia eram poucos. Lia todos ' \
        'os livros, assistia a todos os seminários sobre como prosperar. Eu ' \
        'queria muito ser bem sucedido. Não sabia exatamente se era por' \
        'causa do dinheiro, da liberdade, do sentimento de realização ou ' \
        'apenas para provar a minha capacidade aos meus pais. De qualquer' \
        'modo, vivia obcecado com a idéia de ser "um sucesso". Entre os 20 e' \
        'os 30 anos de idade, comecei vários negócios, sempre com o sonho ' \
        'de fazer fortuna, no entanto os meus resultados foram de fracos a péssimos.'


regex = re.compile("[a-z-áàâãéèêíïóôõöúçñ]+")

dados = regex.findall(texto.lower())

zipf = Counter(dados)

# for c, v in zipf.items():
#     print(f'{c} . {v}')

print(zipf.most_common(10))