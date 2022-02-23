print()

print(f'{" DESAFIO 103 ":+^30}')

print()

def ficha(n = '<desconhecido>', g = '0'):
	if n == '':
		n = '<desconhecido>'
	if g.isnumeric():
		g = int(g)
	else:
		g = 0
	
	
	print(f'O jogador {n} fez {g} gols.')


def lin():
	print('=_-' * 20)

erro = 0

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

lin()

nome = input('Nome do Jogador: ').capitalize().strip()
gols = input('Quantos Gols: ').strip()

lin()
'''
for l in gols:
	if l not in num :
		erro = 1

if erro == 1 or gols == '':
	gols = 0
'''
ficha(nome, gols)

lin()
