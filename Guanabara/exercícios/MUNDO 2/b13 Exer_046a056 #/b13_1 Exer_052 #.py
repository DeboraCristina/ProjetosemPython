print()

print(f'{" DESAFIO 52 ":+^30}')

print()

n = int(input('Número: '))
NdD = 0
primo = ''
for c in range(1, n+1):
	ver = n % c
	if ver == 0:
		NdD += 1
		
if NdD == 2:
	primo = 'É PRIMO'
else:
	primo = 'NÃO É PRIMO'

print()
print()

print('''O número {} foi dividido {} vezes.
Por isso ele {}'''.format(n, NdD, primo))

#com cores
'''n = int(input('Número: '))
NdD = 0
primo = ''
for c in range(1, n+1):
	ver = n % c
	if ver == 0:
		print('\033[33m', end = ' ')
		NdD += 1
	else:
		print('\033[31m', end = ' ')
	print(c, end = ' ')
		
if NdD <= 2:
	primo = 'É PRIMO'
else:
	primo = 'NÃO É PRIMO'

print()
print('\033[30m')

print('O número {} foi dividido {} vezes.\n
Por isso ele {}'.format(n, NdD, primo))'''