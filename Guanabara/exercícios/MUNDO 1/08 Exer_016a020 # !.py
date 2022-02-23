print('-_-_-EXERCICIOS 016 a 020-_-_-')

print()
#
z1 = 'numero real e inteiro'
z2 = 'pitagoras'
z3 = 'seno, coseno e tangente'
z4 = 'de 4, 1'
z5 = 'ordem entre os 4'
z6 = 'mp3'
#


print('===== DESAFIO 16 =====')
print('{:_^40}'.format(z1))
 
#ler um numero real e mostrar sua parte inteira
#ex 1.123 -> 1 (math)

print()

print('===== DESAFIO 17 =====')
print('{:_^40}'.format(z2))
 
#ler o cateto oposto e adjacente de um triangulo retangulo e calcular a hipotenusa.

print()

print('===== DESAFIO 18 =====')
print('{:_^40}'.format(z3))
 
#ler um angulo e mostrar seu seno, coseno e tangente

print()

print('===== DESAFIO 19 =====')
print('{:_^40}'.format(z4))
 
#dentre 4 alunos mostrar um para apagar o quaro

print()

print('===== DESAFIO 20 =====')
print('{:_^40}'.format(z5))
 
#dentre 4 alunos sortear uma ordem para apresentação de um trabalho

print()

print('===== DESAFIO 21 =====')
print('{:_^40}'.format(z6))
 
#reproduzi um arquivo mp3

print()

print(f'{"RESOLUÇÃO":+^30}')

print()

#import para os DESAFIOS 16, 17, 18
from math import floor, pow, sqrt, sin, cos, tan, hypot, radians

print('===== DESAFIO 16 =====')
a = float(input('Insira um número: '))
a1 = floor(a)
print('Convertendo o valor {} para um número inteiro temos: {}.'.format(a,a1))
#Outra maneira seria 'math.trunc(a)'
#Ou 'format(int(a))'

print()

print('===== DESAFIO 17 =====')
bo = float(input('Cateto Oposto: '))
ba = float(input('Cateto Adjacente: '))
bh = hypot(bo, ba)
print('Dimensão do Triangulo:\nCo: {};\nCa: {};\nH: {:.2f}.'.format(bo, ba, bh))
#Minha Solução
#bh = sqrt(pow(bo, 2) + pow(ba, 2))
#triangulo
print('{:>11} \n {:>10} \n {:>10} \n {:>10} \n {:>10} \n {:>10}'.format('/|','/.|','/..|','/...|','/....|','/.....|', '/......|'))

print()

print('===== DESAFIO 18 =====')
c = float(input('Isnsira um Ângulo: '))
cs = sin(radians(c))
cc = cos(radians(c))
ct = tan(radians(c))

print('Angulo: {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangene: {:.2f}'.format(c, cs, cc, ct))
#corrigido

print()
#import para os DESAFIOS 19 e 20
from random import choice, shuffle

print('===== DESAFIO 19 =====')
print('===== DESAFIO 19 =====')
d1 = 'Tanjiro'
d2 = 'Shinubo'
d3 = 'Igoru'
d4 = 'Kanao'
dr = choice([d1, d2, d3, d4])
print('O professor escolheu {} para apagar o quadro'.format(dr))
#outra Solução
'''lista = [d1, d2, d3, d4]
escolhido = choice(lista)
print('O professor escolheu {} para apagar o quadro'.format(escolhido))'''

print()

print('===== DESAFIO 20 =====')
e1 = 'Tanjiro'
e2 = 'Shinubo'
e3 = 'Igoru'
e4 = 'Kanao'
#minha solução
'''er = choices([e1, e2, e3, e4],[1,1,1,1], k=4)
print('Na hora de apresenatar um trabalho na frente da classe, não houve voluntários.\nEntão o professor decidiu que a ordem seria:\n{}'.format(er))'''
#melhor solução
elista = [e1, e2, e3, e4]
shuffle(elista)#shuffle embaralha a lista
print('Na hora de apresenatar um trabalho na frente da classe, não houve voluntários.\nEntão o professor decidiu que a ordem seria:')
print(elista)

print()

print('===== DESAFIO 21 =====')
print('IMPOSSIVEL')
#CORRIGIDO#