print()

print(f'{" DESAFIO 71 ":+^30}')

print()

print('°.+' *  15)
print()
print(F'{"CAIXA ELETRONICO":^45}')
print()
print('°.+' *  15)

print()

valor = float(input('Digite o valor que deseja retirar: '))
print()

mais = 'x'
while mais not in 'sn':
	mais = str(input('Quer retirar notas de R$100 e R$200: [S/N] ')).strip().lower()[0]
print()

while True:
	if mais == 's':
		lobinho = int(valor // 200)
		valor %= 200
		cem = int(valor // 100)
		valor %= 100
	cin = int(valor // 50)
	valor %= 50
	vin = int(valor // 20)
	valor %= 20
	dez = int(valor // 10)
	valor %= 10
	um = int(valor // 1)
	valor %= 1
	
	if valor == 0:
		break


print('As notas a serem retiradas seram: ')
print()

print('°v°.' * 10)
print()

if mais == 's':
	if lobinho != 0:
		if lobinho == 1:
			print(f'{lobinho} nota de R$200 reais')
		else:
			print(f'{lobinho} notas de R$200 reais')
	if cem != 0:
		if cem == 1:
			print(f'{cem} nota de R$100 reais')
		else:
			print(f'{cem} notas de R$100 reais')
if cin != 0:
	if cin == 1:
		print(f'{cin} nota de R$50 reais')
	else:
		print(f'{cin} notas de R$50 reais')
if vin != 0:
	if vin == 1:
		print(f'{vin} nota de R$20 reais')
	else:
		print(f'{vin} notas de R$20 reais')
if dez != 0:
	if dez == 1:
		print(f'{dez} nota de R$10 reais')
	else:
		print(f'{dez} notas de R$10 reais')
if um != 0:
	if um == 1:
		print(f'{um} moeda de R$1 real')
	else:
		print(f'{um} moedas de R$1 real')

print()
print('°v°.' * 10)
print()

aula = 'x'
while aula not in 'sn':
	aula = str(input('Quer ver a solução da aula? [S/N] ')).strip().lower()[0]
print()

if aula == 's':
	valor = float(input('Digite o valor que deseja retirar: '))
	print()
	
	print('As notas a serem retiradas seram: ')
	print()
	
	ced = 50 # maior cédula
	totalced = 0
	
	while True:
		if valor >= ced:
			valor -= ced
			totalced += 1
		else:
			if totalced > 0:
				print(f'{totalced} cédulas de {ced}.')
			if ced == 50:
				ced = 20
			elif ced == 20:
				ced = 10
			elif ced == 10:
				ced = 1
			totalced = 0