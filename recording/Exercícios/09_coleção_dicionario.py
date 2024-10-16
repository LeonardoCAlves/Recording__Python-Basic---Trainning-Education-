notas = {'João': 8.5, 'Maria': 9.0, 'Pedro': 7.5}
aluno = input("Digite o nome de um aluno: ").capitalize()

if aluno in notas:
    print(f"A nota de {aluno} é {notas[aluno]}.")
else:
    print(f"Aluno {aluno} não encontrado. Deseja cadastrá-lo?")
    resposta = input("Digite 'sim' para cadastrar: ").lower()
    if resposta == 'sim':
        nota = float(input(f"Digite a nota de {aluno}: "))
        notas[aluno] = nota
        print(f"Aluno {aluno} cadastrado com nota {nota}.")
    else:
        print("Cadastro não realizado.")
