print()

print(f'{" DESAFIO 84 ":+^30}')

print()

pessoas = []
dados = []
mape = []
mepe = []
maispeso = menorpeso = 0

while True:
	dados.append(input('Nome: '))
	dados.append(float(input('Peso: ')))
	
	# solução da aula (Maior e Menor peso)
	
	if len(pessoas) == 0:
		maispeso = menorpeso = dados[1]
	else:
		if dados[1] > maispeso:
			maispeso = dados[1]
		elif dados[1] < menorpeso:
			menorpeso = dados[1]
	#
	pessoas.append(dados[:])
	dados.clear()
	
	cont = 'x'
	while cont not in 'sn':
		cont = input('Continuar? [S/N] ').strip().lower()[0]
	if cont == 'n':
		break



print(f'Das {len(pessoas)} pessoas cadastradas')
print(f'As mais Pesadas são ', end = '')
for p in pessoas:
	if p[1] == maispeso:
		print(f'[{p[0]}] ', end = '')
print(f'com {maispeso}Kg')
print(f'E as mais leve são ', end = '') 
for p in pessoas:
	if p[1] == menorpeso:
		print(f'[{p[0]}] ', end = '')
print(f'com {menorpeso}Kg')
