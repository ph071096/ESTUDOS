# 3. Considere a seguinte lista = [1,2,3,4,5,6,7,8,9,0]. 
# Percorra a lista e ao final informe a quantidade de pares e ímpares existente nelas.
# Para a lista a cima deve se exibir a seguinte mensagem: "5 pares e 5 ímpares."

numeros = [1,2,3,4,5,6,7,8,9,0]
pares = 0
impares = 0

for i in numeros:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Pares: {pares}')
print(f'Impares: {impares}')