print ('Aula_12')
print ()
print ('-Condições Aninhadas-')
print('#...')
#para uma terceira possibilidade em Condições usa-se o "senãose" = elif
''' 
if condição1
	bloco 1
elif condição2
	bloco 2
else 
	bloco 3'''
#dentro de if pode-se ter quantos elif's quiser
#e o else só uma vez ou nenhuma
print('...#')

print()

print('.Testes.')
nome = str(input('Qual é seu nome? ')).title()

if nome == 'Débora' or nome == 'Debora':
	print('Muito Prazer em te conhecer!!')

elif nome == 'Pedro' or nome == 'Maria':
	print('Que nome comum.')

else:
	print('nome da hora...')
print(f'Tenha um bom dia, {nome}')