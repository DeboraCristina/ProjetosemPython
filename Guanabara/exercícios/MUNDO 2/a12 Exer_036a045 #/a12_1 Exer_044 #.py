print()

print(f'{" Cáculo de desconto ":+^40}')

print()

valor = float(input('Insira o Valor da Compra: '))

print()

print('''Formas de pagamento:

1: A vista (dinheiro ou cheque).
2: A vista no cartão.
3: Em 2x no cartão.
4: Em 3x ou mais no cartão.''')

print()

fp = int(input('Escolha sua opção: '))

if fp == 1:
	valor2 = valor - (valor * 0.1)
elif fp == 2:
	valor2 = valor - (valor * 0.05)
elif fp == 3:
	valor2 = valor
	parcela = valor / 2
	print ('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif fp == 4:
	juros = int(input('Em quantas parcelas pretende pagar: '))
	valor2 = valor + (valor * 0.2)
	parcela = valor2 / juros
	print ('Sua compra será parcelada em {}x de R${:.2f}.'.format(juros, parcela))
else:
	valor2 = 'erro'

print()

if valor2 == 'erro':
	print('Insira uma forma de pagamento válida.')
else:
	print('O Produto que custa {} passará a custar no total {}.'.format(valor, valor2))
	