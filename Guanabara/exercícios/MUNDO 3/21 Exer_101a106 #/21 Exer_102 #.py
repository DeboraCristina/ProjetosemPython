print()

print(f'{" DESAFIO 102 ":+^30}')

print()

def fatorial(n = 1, s = False):
	'''
	|--> Calcula o fatorial de um numero:
		: n: numero a ser fatorado
		: s: [True/False] mostra(ou nao) o calculo.
	'''
	
	f = 1
	print(f'O fatorial de {n} é ', end = '')
	if s == False:
		for c in range(n, 1, -1):
			f *= c
		print(f)
	else:
		for c in range(n, 1, -1):
			f *= c
			if c != 2:
				print(f, end = ' → ', flush = True)
			else:
				print(f'{f}.')
		for c in range(n, 0, -1):
			if c != 1:
				print(f'{c} x ', end = '')
			else:
				print(f'{c} = {f}.')

def lin():
	print('=-' * 20)

lin()

num = int(input('número: '))
show = 'x'
while show not in 'sn':
	show = input('Show? [S/N] ').strip().lower()[0]

lin()

if show == 's':
	show = True
else:
	show = False


fatorial(num, show)

lin()

while True:
	hell = input('Help? [S/N] ').strip().lower()[0]
	if hell in 'ns':
		if hell == 's':
			hell = help(fatorial)
		break
	
