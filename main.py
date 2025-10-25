def autenticar(Login: str, senha: str):
  if Login == 'admin' and senha == '123':
    return 'Sucesso'
  else:
    return 'Incorreto!'
  
print(autentica(Login = 'admin', senha = '123'))
# -------------------------//-------------------------------------

def calcular_media(*args):
  media = sum(args) / len(args)
  return media

print(calcular_media(10, 8))
print(calcular_media(5, 8, 9))
print(calcular_media(5, 6.5, 7, 10))

# -------------------------//-------------------------------------

def exibir_dados(**kwargs):
  for chave, valor in kwargs.items():
    print(f'{chave}: {valor}')
  print('-'*100)

print(exibir_dados(nome='Francisco', idade=21))
print(exibir_dados(nome='Luana', curso='Python', altura=1.65))
print(exibir_dados(nome='Diego', curso='Java Script', endereco='Rua a, 560', data_nascimento='07/10/1996'))

# -------------------------//-------------------------------------

calcular_area = lambda L: L ** 2    #Função lambda
print(calcular_area(5))
print(calcular_area(10))

# -------------------------//-------------------------------------
                #       Quests        #
# 01- Escreva uma função lambda que receba 3 notas e calcule a media e mostre o resultado.

calcular_notas = lambda n1, n2, n3: (n1 + n2 + n3) / 3
print(calcular_notas(5, 6, 9))

# -------------------------//-------------------------------------

# 02- Escreva uma função em lambda que recebe peso e altura, calcume o imc e exiba o resultado.
# Dica: imc = peso / altura**2

calculo_imc = lambda peso, altura: peso / (altura**2)
print(calculo_imc(65, 1.77))

# -------------------------//-------------------------------------
#03- Escreva uma função que recebe base maior, base menor e altura, calcule a área do trapezio e exiba o resultado.
# Dica: area = (base maior + base menor) * altura / 2

def calcular_area(base_maior: float, base_menor: float, altura: float):
  area = (base_maior + base_menor) * altura / 2
  return area

print(calcular_area(2, 5, 1.50))

# -------------------------//-------------------------------------
#04- Escreva uma função lambda que recebe raio e calcula a área do circulo.
# Dica: area = pi * raio**2

calcular_area = lambda raio: 3.14 * (raio**2)
print(calcular_area(2))

# -------------------------//-------------------------------------
#05 - Escreva uma função lambda que recebe horas por parametro e devolva os minutos
# Exemplo => 1 hora => 60 minutos

converter_minutos = lambda horas: horas * 60
print(converter_minutos(5))

# -------------------------//-------------------------------------
par_impar = lambda n: 'Par' if n % 2 == 0 else 'Impar'        #Função lambda que atribui se o numero é Par ou Impar
print(par_impar(5))
print(par_impar(6))
print(par_impar(10))

# -------------------------//-------------------------------------
#06- Escreva uma função lambda que recebe um número e devolve se ele é positivo ou negativo

positivo_ou_negativo = lambda numero: 'Nº Positivo' if numero >= 0 else 'Nº Negativo'
print(positivo_ou_negativo(-1))
print(positivo_ou_negativo(4))
print(positivo_ou_negativo(10))

# -------------------------//-------------------------------------
#07- Escreva uma função lambda que recebe uma velocidade, se ela estiver acima do limite (60) devolva "acima" se estiver dentro do limite devolva "dentro do limite"

limite_velocidade = lambda velocidade: 'Dentro do limite' if velocidade <= 60 else 'Acima do limite'
print(limite_velocidade(80))
print(limite_velocidade(60))
print(limite_velocidade(50))

# -------------------------//-------------------------------------
#08- Escreva uma função lambda que recebe uma idade e devolva "maior de idade" ou "menor de idade"

if_adulto = lambda idade: 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(if_adulto(18))
print(if_adulto(16))
print(if_adulto(20))
print(if_adulto(15))

# -------------------------//-------------------------------------
#09- Escreva uma função lambda que recebe dois números e devolva o maior 

qual_maior = lambda n1,n2: n1 if n1 > n2 else n2
print(qual_maior(2, 5))

# -------------------------//-------------------------------------
#10- Escreva uma função lambda que recebe uma letra e informe se ela é "vogal" ou "consoante"

vogal_ou_consoante = lambda letra: 'Vogal' if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' else 'Consoante'
print(vogal_ou_consoante('a'))
print(vogal_ou_consoante('b'))
print(vogal_ou_consoante('e'))
print(vogal_ou_consoante('p'))

# -------------------------//-------------------------------------
#11- Escreva uma função lambda que recebe um número e informe se ele é "maior que 100" ou "menor que 100"

limite_100 = lambda numero: 'Nº Maior que 100' if numero > 100 else 'Nº Menor que 100'
print(limite_100(101))
print(limite_100(90))
print(limite_100(150))
print(limite_100(50))

# -------------------------//-------------------------------------
#12- Escreva uma função lambda que recebe uma palavra e informe se "tem a letra a" ou "não tem a letra a" nesta palavra 

possui_letra_a = lambda palavra: 'Possui letra "a"' if 'a' in palavra else 'Não possui letra "a"'
print(possui_letra_a('maquina'))
print(possui_letra_a('sonic'))

# -------------------------//-------------------------------------
#13- Escreva uma função lambda que recebe 3 numeros (a, b, c) e devolva "maior" se a soma de a + b for maior que c ou "menor" se a soma não for maior

calculo_abc = lambda n1,n2,n3: 'Maior' if (n1 + n2) > n3 else 'Menor'
print(calculo_abc(5, 4, 5))
print(calculo_abc(2, 4, 10))

# -------------------------//-------------------------------------
#14- Escreva uma função lambda que recebe uma palavra e devolva "tem 6 caracteres" ou "não tem 6 caracteres" 
# Dica: a função len() devolve a quantidade de caracteres

n_palavras = lambda palavra: 'Possui 6 caracteres' if len(palavra) >= 6 else 'Não possui 6 caracteres'
print(n_palavras('MaoKlejada'))
print(n_palavras('Kuja'))
