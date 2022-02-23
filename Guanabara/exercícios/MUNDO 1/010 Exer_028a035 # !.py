print('-_-_-EXERCICIOS 028 a 035-_-_-')

print()
#
z1 = 'jogo de adivinha'
z2 = 'multa'
z3 = 'par ou impar'
z4 = 'preço de passagem'
z5 = 'ano bissexto'
z6 = '> e <'
z7 = 'Aumento justo'
z8 = 'triangulo'
#

print('===== DESAFIO 28 =====')
print('{:+^40}'.format(z1))

#o comput tem que escolher um numero de 0 a 5. e o usuario tem que tentar adivinhar que numero foi
#o comput deve dizer se o usuario acertou ou errou

print()

print('===== DESAFIO 29 =====')
print('{:+^40}'.format(z2))
 
#ler a velocidade de um carro
#se o carro ultrapassar 80km (>80) ele sera multado
#multa = R$7 por km

print()

print('===== DESAFIO 30 =====')
print('{:+^40}'.format(z3))
 
#ler um numero inteiro e mostrar se ele é par ou impar

print()

print('===== DESAFIO 31 =====')
print('{:+^40}'.format(z4))
 
#ler distancia de uma viajem em km. e calcular o preço da passagem
#R$0.50 por km ate 200km e 0.45 para viajens mais longas.

print()

print('===== DESAFIO 32 =====')
print('{:+^40}'.format(z5))
 
#ler um 'ano' e mostrar se ele é bissexto.

print()

print('===== DESAFIO 33 =====')
print('{:+^40}'.format(z6))
 
#ler 3 numeros e mostrar qual é o maior e qual é o menor

print()

print('===== DESAFIO 34 =====')
print('{:+^40}'.format(z7))
 
#ler o salario de um funcionario e calcular seu aumento
# > q R$1250.00, 10%. < 1250 15 %

print()

print('===== DESAFIO 35 =====')
print('{:+^40}'.format(z8))
 
#ler comprimento de 3 retas e mostrar se elas podem ou não formar um triangulo.
#r1: >r2 e r3; (r1 < r2 + r3) = True

print()

print(f'{"RESOLUÇÃO":+^30}')

print()

print('===== DESAFIO 28 =====')
from random import randint
from time import sleep
print('Eu escolhi um numero de 0 a 5.')
a = randint(0,5)
ae = int(input('Adivinhe qual numero eu escolhi: '))
print('PROSSESANDO...')
sleep(2)
if ae == a:
	print('* Você Ganhou *')
else:
	print(f'.Você Perdeu. A resposta era {a}')
print(f'{"FIM":+^11}')

print()

print('===== DESAFIO 29 =====')
bv = float(input('A quanto km/h vc estava? '))
if bv > 80:
	bm = (bv - 80) * 7
	print("Você ultrapassou o limite de velocidade. Sua multa ficara em R${}".format(bm))
else:
	print('PARABÉNS! Você está dentro do limite de velocidade.')

print()

print('===== DESAFIO 30 =====')
c = int(input('Insira um número: '))
print('Par' if c % 2 == 0 else 'Impar')

print()

print('===== DESAFIO 31 =====')
d = float(input('Qual a distancia do seu destino(em km): '))
#minha solução
'''if d <= 200:
	d1 = 0.50 * d
	print('O Preço da sua viajem: R${:.2f}'.format(d1))
else:
	d1 = 0.45 * d
	print('O Preço da sua viajem.: R${:.2f}'.format(d1))'''
#melhor solução
d1 = d * 0.50 if d <= 200 else d * 0.45
print('O Preço da sua viajem.: R${:.2f}'.format(d1))

print()

print('===== DESAFIO 32 =====')
from datetime import date
e = int(input('Insira um ano para avaliar.\nDigite 0 para avaliar o ano atual: '))
if e == 0:
	e = date.today().year

if e % 4 == 0 and e % 100 != 0 or e % 400 == 0:
	print('O ano de {} é um ano BISSEXTO.'.format(e))
else:
	print('O ano de {} não é um ano BISSEXTO.'.format(e))

print()

print('===== DESAFIO 33 =====')
f1 = int(input('Insira o 1º Número: '))
f2 = int(input('Insira o 2º Número: '))
f3 = int(input('Insira o 3º Número: '))

print('O maior valor é: {}'.format(max(f1, f2, f3)))
print('O menor valor é: {}'.format(min(f1, f2, f3)))

print()

print('===== DESAFIO 34 =====')
g = float(input('Insira seu Sálario: R$'))
gr = g + (g * 0.15) if g < 1250.00 else g + (g * 0.10)
print('Seu novo sálario é: {:.2f}'.format(gr))

print()

print('===== DESAFIO 35 =====')
from statistics import median

h1 = float(input('Insira o comprimento da 1ª reta: '))
h2 = float(input('Insira o comprimento da 2ª reta: '))
h3 = float(input('Insira o comprimento da 3ª reta: '))
#minha solução
'''h11 = max(h1, h2, h3)
h22 = median ([h1, h2, h3])
h33 = min(h1, h2, h3)
if h11 < (h22 + h33):
	print('Com os valores {}, {}, {} é possivél formar um triangulo.'.format(h1, h2, h3))
else:
	print('Com os valores {}, {}, {} não é possivél formar um triangulo.'.format(h1, h2, h3))'''
#melhor solução 
if h1 < h2 + h3 and h2 < h1 + h3 & h3 < h1 + h2
	print('Com os valores {}, {}, {} é possivél formar um triangulo.'.format(h1, h2, h3))
else:
	print('Com os valores {}, {}, {} não é possivél formar um triangulo.'.format(h1, h2, h3))
#CORRIGIDO#