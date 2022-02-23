print()

print(f'{" DESAFIO 70 ":+^30}')

print()

total = podutos = mais1000 = menorpreco = 0

nomebarato = ''

while True:
	puduto = input('Nome do produto: ').strip()
	print()
	
	peco = float(input('Preço: R$'))
	print()
	
	podutos += 1	# qntdd d produtos
	total += peco	# valor total
	
	if podutos == 1 or peco < menorpreco:	
		#produto + barato
		nomebarato = puduto
		menorpreco = peco
	if peco > 1000: #produtos + de R$ 1000
		mais1000 += 1
	
	cont = 'x'
	while cont not in 'sn':
		cont = input('Continuar? [S/N] ').lower().strip()[0]
	print()
	if cont == 'n':
		break

print(f'O valor total da compra foi  R${total}.')
print()
print(f'''Dos {podutos} produtos comprados:

{mais1000} produtos custam mais de R$1000.
{nomebarato} é o produto mais barato custando R${menorpreco}.
''')