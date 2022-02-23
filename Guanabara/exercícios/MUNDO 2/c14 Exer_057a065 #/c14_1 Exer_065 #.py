print()

print(f'{" DESAFIO 65":+^50}')

print()

sim = 'S'
l = []
q = m = n = 0
op = 'S'

while sim == 'S':
	while op == 'S':
		n = int(input('numero: '))
		q += 1
		m += n
		l += [n]
		print()
		op = str(input('Quer adicionar mais valores? [S/N] ')).upper().strip()[0]
		print()

	print()

	print('Dos {} valores digitados o maior é {}, o menor é {} e a média entre todos os valores é {:.2f}.'.format(q, max(l), min(l), m/q))
	
	print()
	
	sim = str(input('Quer repitir? [S/N] ')).upper().strip()[0]
	
	print()
	
	if sim == 'S':
		l = []
		q = m = n = 0
		op = 'S'