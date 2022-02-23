print()

print(f'{" DESAFIO 67 ":+^30}')

print()
print()

print(f'{"°+°*"*15:^50}')
print()
print(f'{"Gerador de Tabuadas":^50}')
print()
print(f'{"°+°*"*15:^50}')

print()
print()

cont = 1
while True:
	if cont < 2:
		n = int(input('Digite um Número para saber sua tabuada: '))
	else:
		print('Para Finalizar Digite algum número negativo.')
		n = int(input('Digite outro Número para saber sua tabuada: '))
	cont += 1
	if n <= 0:
		break
	
	print()
	
	print(f'A tabuada de {n} é:')
	
	print()
	
	print('.°' * 6)
	for c in range(1, 11):
		n1 = n * c
		if c < 10 and n1 >= 10:
			print(f'{n} X 0{c} = {n1}')
		elif c < 10 and n1 < 10:
			print(f'{n} X 0{c} = 0{n1}')
		else:
			print(f'{n} X {c} = {n*c}')
	print('.°' * 6)
	
	print()
print()
print('Gerador de Tabuadas Finalizado.')