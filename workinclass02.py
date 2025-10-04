# 2. Solicite 10 letras ao usuário, adicione as vogais em uma lista e exiba a lista no final

from re import A


vogais = []

for letras in range(10):
    letra = input('Digite uma letra: ')
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vogais.append(letra)
        print(vogais)

print(f'Vogais: {vogais}')