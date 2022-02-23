print()

print(f'{" DESAFIO 76 ":+^30}')

print()

carrinho = 'pão', 0.50, 'teclado', 1000.00, 'cabo', 5, 'notboock', 2650, 'cama', 800

c = 0
print('Meu Carrinho')
print()
print('_' * 36)
while True:
	print(f'{carrinho[c].capitalize():.<23}R${carrinho[c+1]:>8.2f}')
	c += 2
	if c >= len(carrinho):
		break
print('_' * 36)


# Solução da aula
'''
t = ('lapis', 2,
'bola', 1,
'tapete', 10,
'bala', 12.50)

for i in range(0, len(t)):
	if i % 2 == 0:
		print(f'{t[i]:.<30}', end = '')
	else:
		print(f'R${t[i]:>8.2f}')
'''