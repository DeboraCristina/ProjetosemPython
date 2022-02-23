print()

print(f'{" DESAFIO 78 ":+^30}')

print()

num = []
for n in range(1,6):
	num.append(int(input(f'Digite o {n}° Número: ')))

print()

print(f'A lista completa: {num}')

print()

print(f'O maior valor da lista: {max(num)} sua posição: ', end = '')
for p in range(0, len(num)):
	if num[p] == max(num):
		print(f'{p + 1}... ', end = '')
print()

print()

print(f'O menor valor da lista: {min(num)} sua posição: ', end = '')
for p in range(0, len(num)):
	if num[p] == min(num):
		print(f'{p + 1}... ', end = '')
print()