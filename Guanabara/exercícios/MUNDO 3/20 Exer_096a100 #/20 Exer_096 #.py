print()

print(f'{" DESAFIO 96 ":+^30}')

print()

def area(h, b):
	a = h * b
	print(f'A área de {h}m X {b}m é {a}m²')


base = float(input('Qual a largura do terreno, em metros: '))
altura = float(input('Qual o comprimento do terreno, em metros: '))

area(base, altura)