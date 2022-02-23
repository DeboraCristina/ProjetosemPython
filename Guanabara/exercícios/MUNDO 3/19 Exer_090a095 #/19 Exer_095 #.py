print()

print(f'{" DESAFIO 95 ":+^30}')

print()

print('o°' * 15)
print()
print(f'{"CADASTRO DE JOGADOR":^30}')
print()
print('o°' * 15)

print()

jogadores = []
jogador = {}

num = ['1', '2', '3', '4', '5', '6', '7', '9', '0']
erro = 0

maior = 0

while True:
	total = 0
	
	jogador['Nome'] = input('Nome: ').capitalize().strip()
	print()
	
	qp = 'x'
	while True:
		erro = 0
		qp = input('Quantas Partidas: ')
		for l in qp:
			if l not in num:
				erro = 1
		if erro == 0:
			break
		print('Digite apenas números.')
		print()
	qp = int(qp)
	
	jogador['Partidas'] = qp
	print()
	
	jogador['Gols'] = []
	
	for g in range(0, qp):
		gol = 'x'
		while True:
			erro = 0
			gol = input(f'Quantos Gols na {g + 1}ª Partida: ')
			for l in gol:
				if l not in num:
					erro = 1
			if erro == 0:
				break
			print('Digite apenas números.')
			print()
		gol = int(gol)
		total += gol
		jogador['Gols'].append(gol)
		print()
	
	if len(jogador['Gols']) >= maior:
		maior = len(jogador['Gols'])
	
	jogador['Total'] = total
	
	jogadores.append(jogador.copy())
	
	resp = 'x'
	while resp not in 'sn':
		resp = input('Quer continuar? [S/N] ').lower().strip()[0]
	print()
	
	if resp == 'n':
		break
	
print('o°' * 30)

print(f'''
{'cód':<5} {'Nome':<20} {'Gols':<18} {'Total':>7}
''')
for i in jogadores:
	print(f'''{jogadores.index(i) + 1:<5} {i['Nome']:<20} {str(i['Gols']):<18} {i['Total']:>7}''')

print()
print('o°' * 30)
print()

while True:
	jog = 'x'
	while True:
		erro = 0
		jog = input('Mostrar Dados do Jogador: ')
		for l in jog:
			if l not in num:
				erro = 1
		if erro == 0:
			break
		print('Digite apenas números.')
		print()
	jog = int(jog)
	print()
	
	if jog == 0:
		break

	if jog <= len(jogadores):
		print(f'-- DADOS DO JOGADOR {jogadores[jog - 1]["Nome"]} --')
		print()
		
		for g in jogadores[jog - 1]["Gols"]:
			if g != 1:
				print(f'Na {jogadores[jog - 1]["Gols"].index(g) + 1}ª partida fez {g} gols.')
			else:
				print(f'Na {jogadores[jog - 1]["Gols"].index(g) + 1}ª partida fez {g} gol.')
			print()
		
		print()
	
	else:
		print('Jogador não encontrado ou cadastrado...')
		print()
print('.*' * 7, f'{"FIM DO PROGRAMA":^17}', '.*' * 7)