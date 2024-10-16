maior_media = 0
menor_media = float('inf')
notas = []

while True:
    nome_aluno = input("\nNome do(a) aluno(a) (ou 'fim' para encerrar): ").title()
    
    if nome_aluno.lower() == 'fim':break
    for i in range(1, 5):
        notas.append(float(input(f"Digite a nota {i} do aluno {nome_aluno}: ")))
    media = sum(notas) / len(notas)
    
    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome_aluno
    
    if media < menor_media:
        menor_media = media
        aluno_menor_media = nome_aluno

print(f"\n\nAluno(a) com maior média: {aluno_maior_media}, Média: {maior_media:.1f}")
print(f"Aluno(a) com menor média: {aluno_menor_media}, Média: {menor_media:.1f}")