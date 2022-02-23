print()

print(f'{" DESAFIO 61":+^50}')

print()

'''
ter = int(input('1º termo: '))
raz = int(input('Razão: '))
dec = (ter + (10 - 1) * raz) + 1

print()

while ter < dec:
	print(ter, end = ' → ')
	ter += raz
print()
'''

# solução da aula
ter = int(input('1º termo: '))
raz = int(input('Razão: '))
cont = 1

while cont <= 10:
	print(ter, end = ' → ')
	ter += raz
	cont += 1
print('FIM')