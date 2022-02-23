print ('Aula_15')
print ()
print ('-Interrompendo Repetição While-')
print()
print('#...')
# Em um 'percurso' maior, a condição de parada acontecerá 'se' tal condição acontecer, caso contrário, os comandos dos percurso aconteceram enquanto ele for verdadeiro.
'''
          T
         --
0          *   *
-----  -----  --- ...
'''

# Ex portugol:
'''
enquanto verdadeiro:
	se tiver chão:
		*passo
	se não tiver chão:
		*pula
	se tiver moeda:
		*pega
	se tiver Troféu:
		*pula
		*interrompe*
*pega
'''

# Ex python:
'''
while True:
	if chão:
		*passo
	if not chão:
		*pula
	if moeda:
		*pega
	if Troféu:
		*pula
		*break*
'''
print('...#')

print()

print('=°'*5, '#Parte Prática#', '=°'*5)

print()

con = 1

while True:
	print(con, end = ' → ')
	con += 1
	if con > 10:
		break
print('Acabou')
