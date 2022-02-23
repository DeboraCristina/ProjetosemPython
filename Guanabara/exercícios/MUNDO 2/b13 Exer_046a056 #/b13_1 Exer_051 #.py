print()

print(f'{" DESAFIO 51 ":+^30}')

print()

print(f'{" Termos de PA ":_^25}')

print()

ter = int(input('Dígite o 1º termo: '))
print()

raz = int(input('Insira a razão da PA: '))
print()

#solução da video aula: 
dec = ter + (10 - 1) * raz

print('Os 10 primeiros termos da PA são:')

print()

#minha solução:
for c in range(ter, (raz*10)+1, raz):
	print(c, end = ' ')
print('.FIM.')

print()

#solução da video aula: *MELHOR*
for c in range(ter, dec + raz, raz):
	print(c, end = ' ')
print('.FIM.')

print()