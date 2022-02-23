print()

print(f'{" DESAFIO 79 ":+^30}')

print()

num = []
while True:
	valor = int(input('Digite um valor: '))
	if valor > 0:
		print('Digite um valor nagativo para PARAR.')
	print()
	
	if valor < 0:
		break
	
	if valor not in num:
		num.append(valor)
		print(f'Valor {valor} adicionado!')
	else:
		print('Valor repitido. valor não adicionado...')
	print()

num.sort()
print(f'''A lista criada foi: {num}
''')
