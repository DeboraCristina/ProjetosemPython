print()

print(f'{" DESAFIO 98 ":+^30}')

print()

from time import sleep

def contador(i, f, r):
	if r < 0:
		r *= -1
	if r == 0:
		print(f'''
{'--' * 20}
ERRO!!
A razão deve ser diferente de ZERO!
A razão vale 1.
{'--' * 20}''')
		r = 1
	
	print()
	print('♣·' * 20)
	print()
	
	print(f'De {i} a {f} de {r} em {r}.')
	print()
	
	if i > f:
		r *= -1
	
	if i < f:
		for c in range(i, f + 1, r):
			if c != f:
				print(c, end = ' → ', flush = True)
			else:
				print(c)
			sleep(0.3)
	else:
		for c in range(i, f - 1, r):
			if c != f:
				print(c, end = ' → ', flush = True)
			else:
				print(c)
			sleep(0.3)
			
	print()
	print('♣·' * 20)
	print()
	sleep(0.3)
	
contador(1, 10, 1)
contador(10, 0, 2)

ini = int(input('Início: '))
fim = int(input('Fim:    '))
raz = int(input('Razão:  '))

contador(ini, fim, raz)