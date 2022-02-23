print()

print(f'{" DESAFIO 68 ":+^30}')

print()

from random import randint

print(f'{"+°*°" * 7:^30}')
print()

print(f'{"Impar ou Par":^30}')

print()
print(f'{"+°*°" * 7:^30}')

print()

c = 0
while True:
	pc = randint(0,10)
	jogador = int(input('numero: '))
	print()
	ip = 'x'
	while ip not in 'IP':
		ip = str(input('impar ou par: [I/P] ')).upper().strip()[0]
		print()
	resultado = pc + jogador
	
	
	if ip == 'P':
		if resultado % 2 != 0:
			print(f'Eu escolhi {pc}. {pc} + {jogador} = {resultado} que é um numero impar')
			break
		else:
			c += 1
			print(f'Eu escolhi {pc}. {pc} + {jogador} = {resultado} que é um numero par')
			print('Parabéns!')
	if ip == 'I':
		if resultado % 2 == 0:
			print(f'Eu escolhi {pc}. {pc} + {jogador} = {resultado} que é um numero par')
			break
		else:
			c += 1
			print(f'Eu escolhi {pc}. {pc} + {jogador} = {resultado} que é um numero impar')
			print('Parabéns!')
			
	print()

print()

print(f'{"Game Over!":^20}')

if c == 1:
	print('Você conquistou 1 vitória!')
else:
	print(f'Você conquistou {c} vitórias!')