print()

print(f'{" DESAFIO 105 ":+^30}')

print()

def inpnum(txt, t = 'i'):
	'''
	input de um número inteiro ou decimal
	: txt: texto dentro do input
	(EX: input(txt))
	: t: tipo de valor:
	i para int
	f para float	
	'''
	if t in 'if':
		if t == 'i':
			num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
			
			erro = False
			
			n = input(txt)
			
			for l in n:
				if l not in num:
					erro = True
			
			if erro:
				return 'erro'
			else:
				return int(n)
			
		if t == 'f':
			num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
			
			erro = False
			f = []
			
			n = input(txt)
			
			for l in n:
				if l == '.' or l == ',':
					f.append(l)
				if l not in num:
					erro = True
			if len(f) > 1:
				erro = True
			
			if erro:
				return 'erro'
			else:
				if ',' in n:
					n1 = float(n.replace(',', '.'))
					return n1
				else:
					return float(n)
	else:
		return 'erro'


def nota(n, sit = False):
	geral = {}
	geral['Quantas Notas'] = len(n)
	geral['Maior'] = max(n)
	geral['Menor'] = min(n)
	geral['Média'] = sum(n) / len(n)
	
	if sit == True:
		if geral['Média'] < 5:
			geral['Situção'] = 'Ruim'
		
		elif 7 >= geral['Média'] >=5:
			geral['Situção'] = 'Boa'
		
		elif geral['Média'] > 7:
			geral['Situção'] = 'Ótima'
	
	return geral


def firula(n = 0):
	if n == 1 or n == 0:
		print()
	if n == 2:
		print('o°' * 30)
	if n == 3:
		print('=-' * 30)
	if n == 4:
		print('--' * 30)
	

t = []

while True:
	
	firula(1)
	firula(2)
	firula(1)
	
	while True:
		no = inpnum('Nota: ', 'f')
		
		if no != 'erro':
			break
		
		firula()
		
		print('Digite algo válido...')
		
		firula(4)
	
	t.append(no)
	
	firula(3)
	
	while True:
		cont = input('Quer continuar? [S/N] ').lower().strip()[0]
		
		if cont in 'sn':
			break
		
		firula()
		
		print('Digite algo válido...')
		
		firula(4)
	
	if cont == 'n':
		break

while True:
	
	firula()
	firula(2)
	
	situ = input('Quer ver a situação? [S/N] ').lower().strip()[0]
	if situ in 'sn':
		firula(2)
		firula()
		break
	
	firula()
	
	print('Digite algo válido...')

if situ == 's':
	situ = True

else:
	situ = False

d = nota(t, sit = situ)

print(d)


