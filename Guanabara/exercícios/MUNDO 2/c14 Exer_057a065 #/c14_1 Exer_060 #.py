print()

print(f'{" DESAFIO 60":+^50}')

print()

n = int(input('Digite um número para saber seu fatorial: '))
n1 = n

# f = 1

print()

print('{}! = '.format(n), end = '')

while n > 0:
	n -= 1
	print(n+1, end = '')
	print(' x ' if n >= 1 else ' = ', end = '')
	if n != 0:
		n1 = n1 * (n)
	''' solução da aula
	print(n+1, end = '')
	print(' x ' if n >= 1 else ' = ', end = '')
	f *= n
	n -= 1
	'''
print('{}'.format(n1))

print()

# Solução da Aula com modulo

aula = input('Quer ver a solução com modulo? [Y/N] ').upper().strip()[0]
if aula == 'Y':
	
	from math import factorial
	
	print()
	
	num =  int(input('Digite um número para saber seu fatorial: '))
	num1 = num
	f = factorial(num)
	
	print()
	
	while num > 0:
		print(num, end = '')
		print(' X ' if num > 1 else ' = ', end = '')
		num -= 1
	print(f)
	print()
	print ('O fatorial de {} é {}.'.format(num1, f))

print()

sfor = input('Quer ver a solução com for? [Y/N] ').upper().strip()[0]

if sfor == 'Y':
	
	print()
	
	v = int(input('Digite um número para saber seu fatorial: '))
	f = 1
	
	print()
	
	for h in range(v, 0, -1):
		print(h, end = '')
		print(' x ' if h > 1 else ' = ', end ='')
		f *= h
	print(f)

print()