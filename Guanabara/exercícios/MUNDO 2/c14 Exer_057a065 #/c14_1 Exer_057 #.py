print()

print(f'{" DESAFIO 57 ":+^30}')

print()

s = ''
#solução da aula
'''while s not in 'MF':'''
while s != 'M' and s != 'F':
	s = input('Insira seu sexo:[M/F] ').upper().strip()[0]
	if s != 'M'  and s != 'F':
		print('Insira uma informação válida...', end = '')
if s == 'M':
	print('Sexo Masculino registrado... ')
if s == "F":
	print('Sexo Feminino registrado...')