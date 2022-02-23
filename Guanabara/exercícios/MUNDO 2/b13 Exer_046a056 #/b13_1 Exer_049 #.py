print()

print(f'{" DESAFIO 49 ":+^30}')

print()

print(f'{" TABUADA ":=^30}')

print()

n = int(input('Dígite um número para saber sua tabuada: '))

print()

print('A TABUADA de {} é:'.format(n))

print()

for c in range(1, 11):
	
	c = str(c)
	c = '{:0>2}'.format(c)
	d = n * int(c)
	d = str(d)
	d = '{:0>2}'.format(d)
	print('{} x {} = {}'.format(n, c, d))

print()