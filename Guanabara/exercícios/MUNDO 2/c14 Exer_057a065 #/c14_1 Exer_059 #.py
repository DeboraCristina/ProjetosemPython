print()

print(f'{" DESAFIO 59 ":+^50}')

print()

from time import sleep

op = 0
n3 = 0

n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))

while op != 5:
	
	
	print('''
[ 1 ] Somar

[ 2 ] Multiplicar

[ 3 ] Mostrar maior

[ 4 ] Novos Números

[ 5 ] Sair
	''')
	op = int(input('Insira sua opção: '))
	
	print()
	
	if op > 5 or op <= 0:
		print('Digite alguma opção válida...')
	
	if op <= 4:
		if op == 1 :
			n3 = n1 + n2
			print('A SOMA entre {} e {} é {}.'.format(n1, n2 , n3))
		elif op == 2:
			n3 = n1 * n2
			print('O número {} X {} é {}.'.format(n1, n2 , n3))
		elif op == 3:
			n3 = max(n1,n2)
			print('Dentre {} e {} o maior número é {}.'.format(n1, n2 , n3))
		elif op == 4:
			print('Digite os novos números.')
			print()
			n1 = int(input('1º Número: '))
			n2 = int(input('2º Número: '))
			op = 0
		sleep (1)
	
# --------------------------------- #
print('Finalizando....')
sleep(1.5)
print('Programa Finalizado.')