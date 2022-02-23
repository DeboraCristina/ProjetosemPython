print()

print(f'{" DESAFIO 58 ":+^50}')

print()

from random import randint

print('{:^50}'.format('Eu pensei em um numero de 1 a 10.'))
print('{:^50}'.format('TENTE ADIVINHAR QUAL É...'))

numero = randint(1,10)
n = numerotentativas = NT = 0

print()
while n != numero:
	NT += 1
	n = int(input('{}º numero: '.format(NT)))
	numerotentativas += 1
	if n != numero and n <= 10:
		if n < numero:
			print('Mais...Tente novamente :P')
		else:
			print('Menos...Tente novamente :P')
	if n > 10:
		print('''WTF?!!!	Eu pensei em um número de 1 a 10! Não de 1 a {}.
		Tente novamente.'''.format(n))

if numerotentativas > 1:
	print('''!!!!Acertou!!!!
Porem vc precisou de {} tentativas para ganhar.KKK'''.format(numerotentativas))
elif numerotentativas == 0:
	print('''!!!ACERTOU!!!
E vc acertou de Primeira!!! 
Q ÓTIMO!!!''')
else:
	print('''!!!ACERTOU!!!
E vc só precisou de {} tentativa!! :)'''.format(numerotentativas))

print()
#solução da aula

cont = str(input('Quer ver a solução da aula?: [Y/N] ')).upper().strip()[0]
if cont == 'Y':
	n = numerotentativas = NT = 0
	acertou = False
	while not acertou:
		NT += 1
		n = int(input('{}º numero: '.format(NT)))
		numerotentativas += 1
		if n == numero:
			acertou = True
		if n != numero and n <= 10:
			if n < numero:
				print('Mais...Tente novamente :P')
			else:
				print('Menos...Tente novamente :P')
		if n > 10:
			print('''WTF?!!!	Eu pensei em um número de 1 a 10! Não de 1 a {}.
		Tente novamente.'''.format(n))
	if numerotentativas > 1:
		print('''!!!!Acertou!!!!
Porem vc precisou de {} tentativas para ganhar.KKK'''.format(numerotentativas))
	elif numerotentativas == 0:
		print('''!!!ACERTOU!!!
E vc acertou de Primeira!!! 
Q ÓTIMO!!!''')
	else:
		print('''!!!ACERTOU!!!
E vc só precisou de {} tentativa!! :)'''.format(numerotentativas))
