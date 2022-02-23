print()

print(f'{" DESAFIO 50 ":+^30}')

print()

soma = 0
pares = 0
for c in range(0, 6):
	n = int(input('Insira o {}º número: '.format(c + 1)))
	print('-_-'*8)
	if n % 2 == 0:
		pares += 1
		soma += n

print()

print('Dos números digitados, {} são pares e a soma entre eles é {}'.format(pares, soma))

print()