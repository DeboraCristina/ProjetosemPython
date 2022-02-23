print()

print(f'{" DESAFIO 53 ":+^30}')

print()

frase = str(input('frase: ')).replace(' ','').upper()
print()
pf = len(frase)

s = frase[:0]

for c in range(pf, 0, -1):
	n = frase[c-1]
	s += n

print('A frase {} ao contrario fica {}'.format(frase,s))
print()

if s == frase:
	print('Essa frase é um palíndromo!')
else:
	print('Essa frase não é um palíndromo.')

