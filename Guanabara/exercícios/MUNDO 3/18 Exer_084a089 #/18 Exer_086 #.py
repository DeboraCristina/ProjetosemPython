print()

print(f'{" DESAFIO 86 ":+^30}')

print()

digitar = 'x'

while digitar not in 'sn':
	digitar = input('Quer digitar valores? [S/N] ').lower().strip()[0]
	print()

if digitar == 's':
	matrix = [[], [], []]

	for i, v in enumerate(matrix):
		for c in range(0, 3):
			v.append(int(input(f'Digite o termo [{i+1}, {c+1}] ')))
		print()
else:
	print('Nah. Tô com Preguiça...')
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print()
print('A matriz formada foi:')
print()

for i, v in enumerate(matrix):
	if i == 0:
		for n in v:
			print(f' [{n:^5}] ', end = '')
	elif i == 1:
		print()
		print()
		for n in v:
			print(f' [{n:^5}] ', end = '')
	elif i == 2:
		print()
		print()
		for n in v:
			print(f' [{n:^5}] ', end = '')
print()
print()

aula = 'x'

while aula not in 'sn':
	aula = input('Quer ver a solução da aula? [S/N] ').lower().strip()[0]

if aula == 's':
	matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]

	for l in range(0, 3):
		for c in range(0, 3):
			matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
	print()
	print('+.o°*' * 10)
	print()
	
	for l in range(0, 3):
		for c in range(0, 3):
			print(f'[{matriz[l][c]:^5}]', end = '')
		print()
	print()
	print('+.o°*' * 10)
	print()