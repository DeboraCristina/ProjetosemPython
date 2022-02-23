print()

print(f'{" DESAFIO 69 ":+^30}')

print()

mais18 = homi = muie20 = pessoas = 0

while True:
	
	idade = int(input('idade: '))
		
	print()
		
	sexo = 'x'
	while sexo not in 'fm':
		sexo = input('sexo: [F/M]').strip().lower()[0]
	
	pessoas += 1
	# pessoas com mais de 18 anos
	if idade >= 18:
		mais18 +=1
		
	# quantos homens
	if sexo == 'm':
		homi += 1
		
	# mulheres com menos de 20 anos.
	if sexo == 'f' and idade <= 20:
		muie20 += 1	
		
	print()
	
	cont = 'x'
	while cont not in 'sn':
		cont = input('continuar? [Sim/Não]').strip().lower()[0]
	
	print()
	
	if cont == 'n':
		break
	
print(f'{"Coleta de dados finalizada...":^40}')

print()

print(f'Das {pessoas} pessoas cadastradas:')

print()
print('-'*70)
print()

if mais18 == 1:
	print(f'	{mais18} Tem mais de 18 anos.')
else:
	print(f'	{mais18} Têm mais de 18 anos.')

print()

if homi == 1:
	print(f'	{homi} homem foi cadastrado.')
else:
	print(f'	{homi} homens foram cadastrados.')

print()

if muie20 == 1:
	print(f'	E {muie20} mulher com menos de 20 anos foi cadastrada.')
else:
	print(f'	E {muie20} mulheres com menos de 20 anos foram cadastradas.')

print()
print('-'*70)
print()
