print ('Aula_14')
print ()
print ('-Estrutura de Repetição While-')
print()
print('#...')
# A estrutura 'for' é util enquanto tiver uma "contagem" -começo e fim-. Quando não se sabe até onde vai o "caminho" usa-se outro estrutura de repetição, q será repetida até acontecer ou não.
# ex: (aula)
''' 
enquanto nao chegar na maça:
	*passo
*pega
'''
# ex: (python)
'''
while not apple:
	*passo
*pega
'''

# Em um caminho sem padrão o while e suas condições são ótimas.

'''
0      *      *   * o
====--==--======--====
'''

# ex: (aula)
'''
enquanto nao chegar na maça:
	se tiver chão:
		*passo
	se tiver buraco:
		*pula
	se tiver moeda:
		*pega
*pega
'''

# ex: (python)
'''
while not apple:
	if chão:
		*passo
	if buraco:
		*passo
	if moeda:
		*pega
*pega
'''
print('...#')

print()

print(f'{"PRÁTICA:+^20"}')

print()

for c in range(1, 11):
	print(c, end = ' ')
print('==FOR==')

print()

b = 1
while b < 11:
	print(b, end = ' ')
	b += 1
print('==WHILE==')

print()

# Nesse caso ambo, 'for' e 'while', são bons em situações onde se sabe um limite.
# Mas em uma situação onde não se sabe o limite 'while' é a melhor solução.
# No caso de querer receber valores até receber o valor correto #

'''n = 1
while n != 666:
	n = int(input('Digite a senha: '))
print('Senha Correta!! Parabéns!')'''

p = 1
par = impar = 0
while p != 0:
	p = int(input('Valor: '))
	if p != 0:
		if p % 2 == 0:
			par += 1
		else:
			impar += 1
print('!! Pares: {}. Impares:{}.'.format(par, impar))
