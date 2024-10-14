"""
Texto por padrão, sempre estaré entre
    ' ' aspas simples
    " " aspas duplas
    ''' ''' aspas simples triplas
    E aspas duplas trilas, como esta que cerca este comentário.
"""

nome = '      LEOnaRdO AlVes    '

print(nome)             # Nome como foi inserida.
print(nome.lower())     # Nome a frase em letras minúsculas.
print(nome.upper())     # Nome em letras maiúsuclas.
print(nome.title())     # Nome com as primeiras letras maiúsculas.
print(nome.strip())     # Nome sem os espaços desnecessários no início e fim.
print(len(nome))        # Total de caracteres, incluindo espaços.
print(nome.count('a'))  # Contando quantas letras 'a' existem no nome.

# Todos os metodos podem ser utilizados na mesma construção.
print(nome.lower().count('a'))

''' Veja abaixo um exemplo de utilização conjunta, onde todo o 
texto é convertido em letras minúsculas para verificar 
quantas letras 'a' existem e os espaços do início e fim 
não são contados. '''

print(nome.strip().lower().count('a'))

