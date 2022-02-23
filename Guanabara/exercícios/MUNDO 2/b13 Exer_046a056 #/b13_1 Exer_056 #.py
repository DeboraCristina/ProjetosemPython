print()

print(f'{" DESAFIO 56 ":+^30}')

print()

mdis = 0 #média de idades

idh = 0  #idade do homem mais velho
nhv = '' #nome do homem mais velho

muie = 0 #quantas mulheres te

for p in range(0, 4):
	print('='*6,'{}ª Pessoa'.format(p+1), '='*6)
	n = str(input('Nome: ')).strip()
	i = int(input('Idade: '))
	s = str(input('Sexo(f/m): ')).strip().upper()
	
	mdis += i
	
	if s == 'M':
		if p == 0:
			nhv = n
			idh = i
		else:
			if i > idh:
				nhv = n
				idh = i
			
	if s == 'F' and i < 20:
			muie += 1
	

mdis = int(mdis / (p+1)) #calculando a média
print()

print('A média de idade do Grupo é de {} anos'.format(mdis))

print('{} é o homem mais velho do grupo, tendo {} anos.'.format(nhv.capitalize(), idh))

if muie <= 1:
	print('{} mulher do grupo tem menos de 20 anos.'.format(muie))
else:
	print('{} mulheres do grupo têm menos de 20 anos.'.format(muie))