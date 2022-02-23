print('===== DESAFIO 38 =====')

from time import sleep


print()

sleep(0.7)
n1 =  int(input('Insira o 1º valor: '))
print()

sleep(0.4)
n2 =  int(input('Insira o 2º valor: '))
print()

sleep(0.7)
if n1 == n2:
	print('Os valores são iguais.')
elif n1 > n2:
	print('O valor {} é maior que {}.'.format(n1, n2))
else:
	print('O valor {} é maior que {}.'.format(n2, n1))