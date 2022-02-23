print('===== DESAFIO 45 =====')

from random import choice
from time import sleep
from stringcolor import *

pc =  choice([1, 2, 3])

sleep(1)
print(cs('Vamos Jogar? :)', '#ff0000').bold())

sleep(1)

print()
print()

print(cs('Escolha:', 'rgb(0, 0, 0)'))
sleep(0.5)
print(cs('[ 1 ] Pedra', 'rgb(0, 255, 255)'))
sleep(0.5)
print(cs('[ 2 ] Papel', 'rgb(255, 164, 255)'))
sleep(0.5)
print(cs('[ 3 ] Tesoura', 'rgb(200, 255, 0)'))
sleep(0.5)

print()

user = int(input(cs('Digite sua opição: ', 'rgb(0, 0, 0)')))


sleep(0.7)
print(cs('JOKEEEEN', '#ff0000').bold())
sleep(1)
print(cs('PÔ', '#ff0000').bold())
sleep(0.5)

if user == pc:
	print(cs('Empate', 'rgb(200,200,200)').bold())
elif user == 1 and pc == 2:
	print(cs('Eu Ganhei!!', 'rgb(255,255,0)').bold())
elif user == 1 and pc == 3:
	print(cs('Você Ganhou!!', 'rgb(0,255,0)').bold())
elif user == 2 and pc == 1:
	print(cs('Você Ganhou!!', 'rgb(0,255,0)').bold())
elif user == 2 and pc == 3:
	print(cs('Eu Ganhei!!', 'rgb(255,255,0)').bold())
elif user == 3 and pc == 1:
	print(cs('Eu Ganhei!!', 'rgb(255,255,0)').bold())
elif user == 3 and pc == 2:
	print(cs('Você Ganhou!!', 'rgb(0,255,0)').bold())
else:
	print(cs('Digite algo valido....', '#ff0000'))

print()

lista = ('pedra', 'papel', 'tesoura')

print('O Computador escolheu {}.'.format(lista[pc - 1]))
print('E o Jogador escolheu {}.'.format(lista[user - 1]))