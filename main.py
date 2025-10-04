# Lista de numeros
lista_numeros = [1, 2, 3, 4, 5, 6]
print(lista_numeros)
print(type(lista_numeros))

#               0         1          2
produtos = [ 'mouse', 'teclado', 'monitor']
print(type(produtos))
print(type(1))
print(type('Olá'))
print(produtos)
print(produtos[1])

produtos[2] = 'monitor 144hz'
print(produtos)

produtos.append('placa de video')
print(produtos)

print('*CADASTRO DE PRODUTO*')
novo_produto = input('Nome: ')
produtos.append(novo_produto)
print(produtos)

produtos.insert(0, 'caixa de som')
print(produtos)

produtos.pop()
print(produtos, '*produtos após o pop()*')
print(produtos.pop(), '*função pop() no print*')
print(produtos)

produtos.remove('mouse')
print(produtos, '*produtos após o remove()*')

for i in produtos:
    if i == 'teclado':
        print(f'{i} existe na lista')
        break
else:
    print('Produto não encontrado')    