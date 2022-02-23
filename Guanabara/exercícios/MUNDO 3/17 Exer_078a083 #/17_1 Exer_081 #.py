print()

print(f'{" DESAFIO 81 ":+^30}')

print()

valores = []
while True:
	valores.append(int(input('Número: ')))
	
	print()
	
	c = 'x'
	while c not in 'sn':
		c = input('Continuar? [S/N] ').strip().lower()[0]
		print()
	if c == 'n':
		break

print(f'''A lista: {valores}
A lista contém {len(valores)} elementos.''')
valores.sort(reverse = True)
print(f'A lista em ordem decreceste: {valores}')
if 5 in valores:
	print('O valor 5 está na lista.')
else:
	print('O valor 5 não está na lista.')