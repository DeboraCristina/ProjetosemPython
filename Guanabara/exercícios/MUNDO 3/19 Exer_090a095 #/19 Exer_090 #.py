print()

print(f'{" DESAFIO 90 ":+^30}')

print()

print('o°*.+' * 6)
print(f'''
{'Cadastro do Aluno':^30}
''')
print('o°*.+' * 6)
print()

pessoa = {}
maz = []
for d in range(0, 11):
	maz.append(str(d))

pessoa['Nome'] = input('Nome do(a) aluno(a): ')
print()

notas = []

n = 'x'
while n not in maz:
	n = input(f'1ª Nota: ')
n = int(n)
print()
notas.append(n)
n = 'x'
while n not in maz:
	n = input(f'2ª Nota: ')
n = int(n)
print()
notas.append(n)


pessoa['Nota'] = notas

pessoa['Média'] = (notas[0] + notas[1]) / 2

if pessoa['Média'] < 5:
	pessoa['Situação'] = 'Reprovado'

elif 5 <= pessoa['Média'] < 7:
	pessoa['Situação'] = 'Recuperação'

elif pessoa['Média'] >= 7:
	pessoa['Situação'] = 'Aprovado'

for k, v in pessoa.items():
	print(f'{k} é {v}')
	print()