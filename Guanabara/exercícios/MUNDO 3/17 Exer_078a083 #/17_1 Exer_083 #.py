print()

print(f'{" DESAFIO 83 ":+^30}')

print()


e = input('Expressão: ')
print()

pe = pd = 0

for i in e:
	if i in '(':
		pe += 1

for h in e:
	if h in ')':
		pd += 1

if pe == pd:
	print('A expressão está correta')
else:
	print('A expressão está incorreta')
	
# outra solução:
'''
e = input('Expressão: ')
print()
if e.count('(') == e.count(')'):
	print('A expressão está correta')
else:
	print('A expressão está incorreta')
'''