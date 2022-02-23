print()
print('===== DESAFIO 42 =====')
print()

from statistics import median

h1 = float(input('Insira o comprimento da 1ª reta: '))
print()

h2 = float(input('Insira o comprimento da 2ª reta: '))
print()

h3 = float(input('Insira o comprimento da 3ª reta: '))
print()

if h1 < h2 + h3 and h2 < h1 + h3 and h3 < h1 + h2:
	print('Com os comprimentos acima é possivél formar um triangulo.'.format(h1, h2, h3))
	if h1 == h2 == h3:
		print('O triangulo formado é um triangulo EQUILÁTERO.')
	elif h1 != h2 != h3 != h1:
		print('O triangulo formado é um triangulo ESCALENO.')
	else:
		print('O triangulo formado é um triangulo ISÓCELES.')

else:
	print('Com os comprimentos acima não é possivél formar nenhum triangulo.'.format(h1, h2, h3))

