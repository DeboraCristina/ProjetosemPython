print()

print(f'{" DESAFIO 66 ":+^30}')

print()

c = s = 0

while True:
	if c <= 1:
		n = int(input('Insira um número: '))
	else:
		n = int(input('Insira outro número: '))
	print('...Digite *999* para parar...')
	print()
	if n == 999:
		break
	c += 1
	s += n

print()

if c > 1:
	print(f'Você digitou {c} números e a soma entre eles é {s}.')
else:
	if c == 0:
		print(f'Você digitou {c} números.')
	if c == 1:
		print(f'Você digitou {c} número.')
		
print()