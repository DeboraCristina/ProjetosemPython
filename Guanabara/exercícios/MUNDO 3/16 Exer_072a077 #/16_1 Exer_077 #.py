print()

print(f'{" DESAFIO 77 ":+^30}')

print()

t = 'Casa', 'Mundo', 'Olá', 'Tchau'
for p in t:
	print(f'Na palavra * {p.upper()} * tem as vogais: ', end = ' ')
	for l in p:
		if l in 'aáeéiíoóuú':
			print(l, end = ' ')
	print()
	print(' -' * 20)
	
