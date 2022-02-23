'''
desafios
'pintar' 2 exercicios que já foram feitos.
fazer 2 programas coloridos com tudo que já foi aprendido
'''

print('\033[36m' + f'{"DESAFIO 23":+^20}')
cores = {'amarelo': '\033[33m',
		 'roxo': '\033[35m',
		 'verde': '\033[32m',
		 'vermelho': '\033[31m',
		 'vazio': '\033[m'}
a = str(input('\033[34mIsira um número: \033[m')).replace(' ', '')
a = '{:0>4}'.format(a)
au = '\033[30m' + a[3] + '\033[m'
ad = '\033[37m' + a[2] + '\033[m'
ac = '\033[30m' + a[1] + '\033[m'
am = '\033[37m' + a[0] + '\033[m'
print('{}Unidade: {} {}'.format(cores['amarelo'], cores['vazio'], au))
print('{}Dezena: {} {}'.format(cores['roxo'], cores['vazio'], ad))
print('{}Centena: {} {}'.format(cores['verde'], cores['vazio'], ac))
print('{}Milhar:{} {}'.format(cores['vermelho'], cores['vazio'], am))

print()

print('\033[36m' + f'{"DESAFIO 27":+^20}')
b = str(input('\033[34mColoque seu nome completo: \033[m')).strip().title().split()
b1 = '\033[7;33m' + b[0] + '\033[m'
b2 = '\033[7;33m' + b[len(b) - 1] + '\033[m'
print('O seu \033[32mPrimeiro\033[m nome é {} e o \033[36mútimo\033[m é {}.'.format(b1, b2))

print()

nome = str(input('\033[36m' + 'Digite seu nome: ')).upper().strip()
idade = int(input('\033[36m' + 'E a sua idade: '))
if nome.split()[0] == 'DÉBORA':
	print('\033[1;33mMas que nome maravilhoso!\033[m ', end='')
print('\033[30mPrazer te conhecer, {}!'.format(nome.title()))
print('Sua idade é: {}. \033[m'.format(idade), end='')
if idade < 13:
	print('Você é criança.')
if idade >= 13 and idade <= 17:
	print('Você é adolecente.')
if idade >= 18:
	print('Você é adulto.')

print()

from random import randint
from time import sleep
pontos = 0
print('\033[30mEu pensei em um número de 1 a 10')
pc = randint(1, 10)
print('O número que eu pensei vezes 7 é: {}\033[m'.format(pc * 7))
user = str(input('\033[1m\033[7;30mAdivenhe qual número eu pensei:\033[m ')).replace(' ', '')
user = int(user)

if user == pc:
	pontos = pontos + 1
	print('\033[1;33;36m!!GANHOU!!\033[m')
	print('\033[31m' + f'{"-_-":^10}' + '\033[m')
	print('\033[1;31mP A R A B É N S\033[m\n\033[31mQue tal mais uma rodada?\033[m')
else:
	print('\033[1m\033[4;31mVocê PERDEU!!\033[m\n\033[1;33mP E R D E U !!')
	sleep(1)
	print('.')
	sleep(1)
	print('.')
	sleep(1)
	print('.')
	sleep(0.5)
	print('P')
	sleep(0.5)
	print('E')
	sleep(0.5)
	print('R')
	sleep(0.5)
	print('D')
	sleep(0.5)
	print('E')
	sleep(0.5)
	print('U\033[m')
	sleep(0.5)
	print('\033[33mQue PENA. Vou te dar mais uma chance.\033[m')
print('\033[30mAgora eu pensei em outro número de 1 a 10')
pc = randint(1, 10)
print('O número que eu pensei vezes 7 mais 7 é: {}\033[m'.format((pc * 7)+7))
user = str(input('\033[1m\033[7;30mAdivenhe de novo:\033[m ')).replace(' ', '')
user = int(user)
if user == pc:
	pontos = pontos + 1
	print('\033[1;33;36m!!GANHOU!!\033[m')
	print('\033[31m' + f'{"-_-":^10}' + '\033[m')

else:
	print('\033[1m\033[4;31mVocê PERDEU!!\033[m\n\033[1m\033[1;33m !!')
	sleep(1)
	print('.')
	sleep(1)
	print('.')
	sleep(1)
	print('.')
	sleep(0.5)
	print('P')
	sleep(0.5)
	print('E')
	sleep(0.5)
	print('R')
	sleep(0.5)
	print('D')
	sleep(0.5)
	print('E')
	sleep(0.5)
	print('U\033[m')
print('\033[1;36m' + '{:=^30}'.format('FIM'))
print('Você fez {} pontos.\033[m'.format(pontos))