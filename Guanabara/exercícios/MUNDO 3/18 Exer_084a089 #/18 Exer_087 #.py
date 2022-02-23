print()

print(f'{" DESAFIO 87":+^30}')

print()

digitar = 'n'
while digitar not in 'sn':
	digitar = input("Quer digitar valores? [S/N] ").lower().strip()[0]

maior = pares = tco = 0

if digitar == 's':
	matrix = [[], [], []]

	for i, v in enumerate(matrix):
		for c in range(0, 3):
			v.append(int(input(f'Digite o termo [{i+1}, {c+1}] ')))
		print()
else:
	print()
	print('Nah. Tô com Preguiça...')
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print()

print('A matriz formada foi:')
print()
print('-=' * 20)
for i, v in enumerate(matrix):
	if i == 0:
		tco += v[2]
		for n in v:
			if n % 2 == 0:
				pares += n
			print(f' [{n:^5}] ', end = '')
		print()
	elif i == 1:
		print()
		maior = max(v)
		tco += v[2]
		for n in v:
			if n % 2 == 0:
				pares += n
			print(f' [{n:^5}] ', end = '')
		print()
	elif i == 2:
		print()
		tco += v[2]
		for n in v:
			if n % 2 == 0:
				pares += n
			print(f' [{n:^5}] ', end = '')
		print()

print(f'''{'-=' * 20}

O maior valor da segunda linha foi {maior}
A soma da terceira coluna é {tco}
A soma dos pares é {pares}
''')

aula = 'x'
while aula not in 'sn':
	aula = input('Quer ver a solução da aula? [S/N] ').lower().strip()[0]

if aula == 's':
	maior = pares = tco = 0
	matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

	for l in range(0, 3):
		for c in range(0, 3):
			matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
	print('=-' * 20)
	for l in range(0, 3):
		tco += matriz[l][2]
		if l == 1:
			maior += max(matriz[l])
		for c in range(0, 3):
			print(f'[{matriz[l][c]:^5}]', end = '')
			if matriz[l][c] % 2 == 0:
				pares += matriz[l][c]
		print()
	print('=-' * 20)
	print(f"A soma dos pares é {pares}")
	print(f'A soma dos valores da 3ª coluna é {tco}')
	print(f'O maior valor da 2ª linha é {maior}')