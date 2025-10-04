# 1. Solicite 10 números ao usuário, adicione os pares em uma lista e o impares em outra, 
# exiba as duas lista no final.
pares = []
impares = []
numeros = []

for i in range(10):
    numeros = float(input('Numero: '))
    if numeros % 2 == 0:
        pares.append(numeros)
        print(pares)
    else:
        impares.append(numeros)
        print(impares)
print(f'Impares: {impares}')
print(f'Pares: {pares}')