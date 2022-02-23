print()

print(f'{" DESAFIO 100 ":+^30}')

print()

from random import randint
from time import sleep

num = [] 

def sorteia(lis):
	lis.clear()
	
	print()
	print(f'{"SORTEANDO 5 VALORES":^30}')
	print()
	
	print('Os números sorteados foram: ', end = '')
	
	c = 1
	
	while len(lis) < 6:
		n = randint(1, 10)
		if n not in lis:
			if c < 5:
				print(n, end = ' → ', flush = True)
			else:
				print(n, end = '.', flush = True)
			c += 1
			sleep(0.3)
			lis.append(n)
		if len(lis) == 5:
			break
	
	print()

def somapar(lst):
	pares = []
	
	for v in lst:
		if v % 2 == 0:
			pares.append(v)
	
	print('Os números pares são foram: ', end = '')
	
	con = 1
	
	for p in pares:
		if con < len(pares):
			print(p, end = ' → ', flush = True)
		else:
			print(p, end = '.', flush = True)
		sleep(0.3)
		con += 1
	
	print()
	
	print(f'E a soma entre eles é: {sum(pares)}')
	
	print()

sorteia(num)
somapar(num)

sorteia(num)
somapar(num)

sorteia(num)
somapar(num)

sorteia(num)
somapar(num)
