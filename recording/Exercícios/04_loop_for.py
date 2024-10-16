total_idade_homens = 0
total_idade_mulheres = 0
total_renda_homens = 0
total_renda_mulheres = 0
cont_homens = 0
cont_mulheres = 0
pessoa_maior_renda = ""
maior_renda = 0

for i in range(2):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo (M/F): ")).upper()
    renda = float(input("Digite a renda mensal: "))

    if sexo == 'M':
        total_idade_homens += idade
        total_renda_homens += renda
        cont_homens += 1

    elif sexo == 'F':
        total_idade_mulheres += idade
        total_renda_mulheres += renda
        cont_mulheres += 1
    
    if renda > maior_renda:
        maior_renda = renda
        pessoa_maior_renda = nome
    
media_idade_homens = total_idade_homens / cont_homens if cont_homens > 0 else 0
media_idade_mulheres = total_idade_mulheres / cont_mulheres if cont_mulheres > 0 else 0
media_idade_geral = (total_idade_homens + total_idade_mulheres) / (cont_homens + cont_mulheres)
media_renda_homens = total_renda_homens / cont_homens if cont_homens > 0 else 0
media_renda_mulheres = total_renda_mulheres / cont_mulheres if cont_mulheres > 0 else 0
media_renda_geral = (total_renda_homens + total_renda_mulheres) / (cont_homens + cont_mulheres)

print("\n\nResultados da Pesquisa:")
print(f"Média de idade dos homens: {media_idade_homens:.2f}")
print(f"Média de idade das mulheres: {media_idade_mulheres:.2f}")
print(f"Média de idade geral: {media_idade_geral:.2f}")
print(f"Média de renda dos homens: {media_renda_homens:.2f}")
print(f"Média de renda das mulheres: {media_renda_mulheres:.2f}")
print(f"Média de renda geral: {media_renda_geral:.2f}")
print(f"Pessoa com a maior renda: {pessoa_maior_renda} (renda: {maior_renda:.2f})")