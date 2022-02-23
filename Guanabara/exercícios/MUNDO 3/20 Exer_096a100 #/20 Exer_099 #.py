print()

print(f'{" DESAFIO 99 ":+^30}')

print()

from time import sleep

def maior(*num):
	if len(num) > 0:
		m = max(num)
	
	print('+.*' * 20)
	print()
	
	print('Analizando', end = '', flush = True)
	sleep(0.5)
	print('.', end = '', flush = True)
	sleep(0.5)
	print('.', end = '', flush = True)
	sleep(0.5)
	print('.', end = '', flush = True)
	sleep(0.5)
	print()
	print()
	
	if len(num) >= 2:
		print('Os valores recebidos foram: ', end = '')
		
		c = 1
		
		for n in num:
			if c <= len(num) - 1:
				print(n, end = ' → ', flush = True)
			
			else:
				print(n, end = '. ', flush = True)
			
			c += 1
			sleep(0.3)
		
		print()
		print(f'Dos {c-1} Valores recebidos. O maior deles é o {m}.')
	
	elif len(num) == 0:
		print('Nenhum Valor foi recebido')
	
	else:
		print(f'O valor recebido foi: {num[0]}')
		print(f'Dos Valores recebidos. O maior deles é o {num[0]}.')
	
	print()
	

maior(9, 3, 5, 4, 10)
maior(4, 0, 2)
maior(2, 2)
maior(9)
maior()