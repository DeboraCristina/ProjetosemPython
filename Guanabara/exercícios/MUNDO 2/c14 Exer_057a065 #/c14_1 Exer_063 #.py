print()

print(f'{" DESAFIO 63":+^50}')

print()
print()

print('=°=' * 11)
print()

print('{:^30}'.format('Sequência de Fibonacci'))

print()
print('=°=' * 11)

print()

op = 1
n = raz = 0
valor = int(input('Quantos números você quer ver? '))
lista = [] # lista e contador, da na msma

print()

while op != 0:
	print(n, end = ' → ')
	n += raz
	raz = n -  raz
	lista += ['a']
	if n == 0:
		n += 1
	if len(lista) >= valor:
		op = 0
print('Fim da Sequência.')
