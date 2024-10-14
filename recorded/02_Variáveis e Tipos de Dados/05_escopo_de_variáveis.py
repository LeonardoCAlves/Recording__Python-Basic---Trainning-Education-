"""
Escopo >>> Limitação de espaço
Escopo de variáveis >>> Está variável vai ser reconhecida apenas dentro do escopo onde foi declarada

Variavel Global >>> Pode ser utilizada em qualquer parte do código
Variavel Local >>> Pode ser utilizada dentro do local onde foi declarada
"""

def Cadastro():
    nome = 'Maria'  # Variável local
    return nome  # Necessário retorná-la para acesso fora do escopo.


while True:
    print('a')

nome = 'Leonardo'  # variável global, possível acessá-la em qualquer parte do código.

print(nome)

print(Cadastro())  # Print já instanciando a função Cadastro