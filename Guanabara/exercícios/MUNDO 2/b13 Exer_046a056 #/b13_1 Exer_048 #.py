print()

print(f'{" DESAFIO 48 ":+^30}')

print()

# 2 3 5 7 11 13 17 19 23 29 31

s=0
cont = 0 

for c in range(1, 501, 2):
	if c % 3 == 0:
		cont += 1
		s += c
print('A soma entre os {} números é: {}'.format(cont, s))