print()

print(f'{" DESAFIO 85 ":+^30}')

print()

num = [[], []]

for v in range(0, 7):
	valor = int(input('Digite um número: '))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)

num[0].sort()
num[1].sort()

print(f'''
{'+.o°*' * 10}

Os números pares {num[0]}
Os números impares {num[1]}

{'+.o°*' * 10}
''')