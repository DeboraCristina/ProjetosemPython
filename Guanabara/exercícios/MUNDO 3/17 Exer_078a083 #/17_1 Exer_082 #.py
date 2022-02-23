print()

print(f'{" DESAFIO 82 ":+^30}')

print()


l1 = []
lp = []
li = []

while True:
	v = int(input('Número: '))
	if v < 1:
		break
	l1.append(v)
	if v % 2 == 0:
		lp.append(v)
	else:
		li.append(v)
	

print(f'''
Lista completa: {l1}
Lista dos pares: {lp}
Lista dos impares: {li}
''')