print()

print(f'{" DESAFIO 75 ":+^30}')

print()

t = ()
for c in range(1, 5):
	if c == 1:
		n = int(input('Digite um Número: ')),
	elif c == 4:
		n = int(input('Digite o último Número: ')),
	else:
		n = int(input('Digite mais um Número: ')),
	print()
	t += n
print(f'''
A lista criada foi {t}.

O número 9 apareceu {t.count(9)} vezes.
''')

if 3 in t:
	print(f'A Primeira vez que o número 3 apareceu foi na {t.index(3)+1}ª posição.')
else:
	print(f'O número 3 apareceu {t.count(3)} vezes.')


print('''
Os números pares são: ''', end = '' )

for k in t:
	if k % 2 == 0:
		print(k, end = ', ')
print()
print()
