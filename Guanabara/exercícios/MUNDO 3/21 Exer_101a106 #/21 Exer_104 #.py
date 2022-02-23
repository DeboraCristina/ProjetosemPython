print()

print(f'{" DESAFIO 104 ":+^30}')

print()

def leianum(txt):
	
	from stringcolor import cs
	
	num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
	
	while True:
		t = input(txt).strip()
		ERRO = 0
		flow = []
		vir = 0
		
		for l in t:
			if l == '.' or l == ',':
				flow.append(l)
			if l not in num:
				ERRO = 1
		
		if len(flow) > 1 or t == '':
			ERRO = 1
			
		
		if ERRO == 0:
			if '.' in t:
				t = float(t)
			elif ',' in t:
				t1 = float(t.replace(',', '.'))
				vir = 1
			else:
				t = int(t)
			break
		
		print(cs('ERRO! Tente novamente...', 'magenta'))
	if vir == 0:
		return t
	else:
		return t1


n = leianum('Número: ')

print(f'''
O número {n} é multiplo de {n * 2}.''')
