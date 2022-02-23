print()

print(f'{" DESAFIO 89 ":+^30}')

print()

sala = []
aluno = []
nota = []


ver = []
veri = []

for a in range(0, 11):
	ver.append(str(a))
for num in range(0, 1001):
	veri.append(str(num))

'''sala = [['ana', [2, 8], 5], ['jorge', [4, 10], 7], ['Lava', [10, 8], 9]]'''

while True:
	aluno.append(input('Nome: '))
	n = 'x'
	while n not in ver:
		n = input('1º Nota: ')
	n = int(n)
	nota.append(n)
	n = 'x'
	while n not in ver:
		n = input('2º Nota: ')
	n = int(n)
	nota.append(n)
	
	aluno.append(nota[:])
	aluno.append((nota[0] + nota[1]) / 2)
	
	sala.append(aluno[:])
	
	aluno.clear()
	nota.clear()
	
	c = 'x'
	while c not in 'sn':
		c = input('Quer continuar? [S/N] ').strip().lower()[0]
	if c == 'n':
		break

print()
print('=_-' * 10)
print()

print(f'''{'N°':<4}{'Nomes':<10}{'Médias':<8} 
{'-' * 20}''')

for a in sala:
	print(f"{sala.index(a) + 1:<4}{sala[sala.index(a)][0]:<10}{sala[sala.index(a)][2]:<8.1f}")
print('-' * 20)

while True:
	cont = 'x'
	while cont not in veri:
		cont = input('Quer ver a nota de qual aluno? (Digite 0 para Parar) ')
	cont = int(cont)
	print()
	
	
	if cont == 0:
		break
	if cont <= len(sala):
		print(f'As notas de {sala[cont - 1][0]} são {sala[cont - 1][1]}')
	else:
		print('Esse(a) aluno(a) não está na lista')
	print()

print()

print('FIM DO PROGRAMA DE NOTAS')