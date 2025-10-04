# Solicitar ao usuario o nome de 5 produtos e no final exiba essa lista
produtos = []
print('*Cadastre 5 produtos*')

for i in range(5):
    cadastro_produto = input('Produto: ')
    produtos.append(cadastro_produto)

print(produtos)