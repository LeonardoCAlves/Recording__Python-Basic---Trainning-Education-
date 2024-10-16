frutas = ('maçã', 'banana', 'laranja', 'uva', 'manga')
fruta = input("Digite o nome de uma fruta: ").lower()

if fruta in frutas:
    print(f"{fruta.capitalize()} está na lista de frutas!")
else:
    print(f"{fruta.capitalize()} não está na lista de frutas.")
    print("Frutas disponíveis:", ', '.join(frutas))
