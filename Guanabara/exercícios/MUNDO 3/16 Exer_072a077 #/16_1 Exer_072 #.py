print()

print(f'{" DESAFIO 72 ":+^30}')

print()

ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
	while True:
		num = int(input('Escola um número entre 0 e 20: '))
		if num >= 0 and num <= 20:
			break
		else:
			print('Tente de novo.')
	 
	while True:
		print('''
[ 1 ] Tudo MAIÚSCULO
[ 2 ] Tudo minúsculo
[ 3 ] Primeira Letra Maiúsculo
		''')
		op = int(input('opçao: '))
			
		if op >= 1 and op <= 3:
			break
	print()

	if op == 1:
		print(f'Você escolheu o número *{ext[num].upper()}*.')
	if op == 2:
		print(f'Você escolheu o número *{ext[num].lower()}*.')
	if op == 3:
		print(f'Você escolheu o número *{ext[num].capitalize()}*.')
	print()
	
	con = 'x'
	while con not in 'sn':
		con = input('Quer continuar? [S/N] ').lower().strip()[0]
	print()
	if con == 'n':
		break

print('Fim do programa')