print()

print(f'{" DESAFIO 62":+^50}')

print()

print('Termos em uma Progressão Aritimética')

ter = int(input('1º Termo: '))
raz = int(input('Raizão: '))
cont = 1
qt = 10
m = 0

print()

while qt != 0:
	print(ter, end = ' ')
	cont += 1
	ter += raz
	m += 1
	if cont > qt:
		print()
		print()
		qt = int(input('Quer mostrar mais quantos termos: '))
		print()
		cont = 1
		print('Os próximos {} termos da PA são...'.format(qt))
print('Progressão Finalizada com {} termos.'.format(m))