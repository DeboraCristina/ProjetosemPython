print()

print(f'{" DESAFIO 88 ":+^50}')

print()

from time import sleep 
from random import randint

print(f'''{"Digite quantas cartela deseja sortear":^50}
''')

geração = []
tabelas = []
jogo = 'x'
num = []

for c in range(0, 10001):
	num.append(str(c))
#print(num)

while jogo not in num:
	jogo = input('Digite um número : ')
jogo = int(jogo)

print()
print('_-' * 25)
print()

for t in range(0, jogo):
	while len(geração) < 6:
		pc = randint(1, 60)
		if pc not in geração:
			geração.append(pc)
	geração.sort()
	tabelas.append(geração[:])
	geração.clear()
	sleep(0.5)
	print(f'Jogo {t + 1}: {tabelas[t]}')
	print('_-' * 25)
print()
sleep(0.5)
print(f"{'Boa Sorte!!!':^50}")