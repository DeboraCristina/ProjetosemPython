print()

print(f'{" DESAFIO 93 ":+^30}')

print()

print('o°' * 15)
print()
print(f'{"CADASTRO DE JOGADOR":^30}')
print()
print('o°' * 15)

print()

jogador = {}

jogador['Nome'] = input('Nome do Jogador: ').capitalize().strip()
print()

jogador['Quantidade de Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
print()

jogador['Quantidade de Gols'] = {}
print(f'Quantos Gols {jogador["Nome"]} fez na')
print()

for p in range(0, jogador['Quantidade de Partidas']):
	jogador['Quantidade de Gols'][f'{p+1}ª Partida'] = int(input(f'{p+1}ª Partida: '))
	print()

for t, i in jogador.items():
	if t == 'Nome':
		print(f'O {t} é {i}.')
		print()
		
	elif t == 'Quantidade de Partidas':
		print(f'Jogou {i} Partidas')
		print()
		
	elif t == 'Quantidade de Gols':
		for k, v in jogador['Quantidade de Gols'].items():
			print(f'Na {k} foram {v} gols.')
			print()
print()