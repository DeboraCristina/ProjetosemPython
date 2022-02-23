print()

print(f'{" DESAFIO 94 ":+^30}')

print()

pes = []
dados = {}

num = []
for a in range(0, 101):
	num.append(str(a))

c = 0
somaid = 0

mulheres = []

while True:
	dados['Nome'] = input('Nome: ').capitalize().strip()
	
	s = 'x'
	while s not in 'FM':
		s = input('Sexo: [F/M] ').upper().strip()[0]
		if s not in 'FM':
			print('Por favor digite apenas F ou M.')
	
	dados['Sexo'] = s
	
	if dados['Sexo'] == 'F':
		mulheres.append(dados['Nome'])
	
	i = 'x'
	while i not in num:
		i = input('Idade: ')
		if i not in num:
			print('Por favor digite apenas números.')
	i = int(i)
	
	dados['Idade'] = i
	
	somaid += dados['Idade']
	
	pes.append(dados.copy())
	dados.clear()
	
	print()
	cot = 'x'
	while cot not in 'sn':
		cot = input('Quer continuar? [S/N] ').lower().strip()[0]
		if cot not in 'sn':
			print('Por favor digite apenas S ou N.')
	
	print('=-' * 15)
	
	c += 1
	
	if cot == 'n':
		break
	
	
	
if c > 1:
	média = somaid / c

print()

if c > 1:
	print(f' - {c} pessoas foram casdastradas.')
	print()
else:
	print(f' - {c} pessoa foi casdastrada.')
	print()

if c > 1:
	print(f' - A média de idade é de {média:.0f} anos.')
	print()

print(' - As mulheres cadastradas foram: ', end = '')
nm = 1
for p in mulheres:
	if nm < len(mulheres):
		print(p, end = ', ')
	else:
		print(p, end = ' ')
	nm += 1
print()
print()

print(' - Lista das pessoas com idade acima da média: ')
print()

if c > 1:
	for p in pes:
		if p['Idade'] > média:
			for k, v in p.items():
				if k != 'Idade':
					print(f'{k} = {v}', end = ', ')
				else:
					print(f'{k} = {v}')
			print()
