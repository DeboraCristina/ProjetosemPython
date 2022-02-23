print()

print(f'{" DESAFIO 74 ":+^30}')

print()

from random import randint

t = ()

while True:
	pc = randint(1, 9),
	t += pc
	if len(t) >= 5:
		break
print(f'''A lista Sorteaida foi: {t}
O Maior valor foi: {max(t)}.
O Menor valor foi: {min(t)}.
''')

aula = 'x'
while aula not in 'sn':
	aula = ('Quer ver a solução da aula? [S/n] ').lower().strip()[0 ]


if aula == 's':
	pc = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
	print(f'''A lista Sorteaida foi: {pc}
O Maior valor foi: {max(pc)}.
O Menor valor foi: {min(pc)}.
	''')