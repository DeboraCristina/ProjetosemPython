print()

print(f'{" DESAFIO 64":+^50}')

print()

n = q = s = 0

while n != 999:
	if q == 0:
		tex = 'Digite um número: '
	else:
		tex = 'Digite outro número: '
	n = int(input('{}'.format(tex)))
	print('Para encerrar digite 999.')
	print()
	if n != 999:
		q += 1
		s += n

print()

print('!!!Fim do Programa!!!')

print()

if q == 0:
	print('Você não digitou nenhum número...')
else:
	print('Você digitou {} números e a soma entre eles é {}.'.format(q, s))

print()