## sistema para verificar se foi digitado um número ou um texto ##

# V.1 (Tem limete de números e trabalha só com números inteiros)
'''
jogo = 'x'
num = []

for c in range(0, 11):
	num.append(str(c))
#print(num)

while jogo not in num:
	jogo = input('Digite um número : ')
jogo = int(jogo)

print('break')
print(jogo * 2)

# V.2 (Não tem limete de números e trabalha com números decimais e inteiros), sem ','

while True:
	frase = input('número: ')
	num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
	val = 0
	for l in frase:
		if l not in num:
			val = 1
	if val != 1:
		frase = float(frase)
		break
	print('Digite algo válido')
print('fim')
print(frase + 3.5)

# V.3 float com ','

frase2 = ''
while True:
	frase = input('número: ')
	num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
	val = 0
	for l in frase:
		if l not in num:
			val = 1
		if val == 0:
			if l == ',':
				frase2 = frase.replace(',', '.')
	if val != 1:
		if ',' in frase:
			frase2 = float(frase2)
		else:
			frase2 = float(frase)
		break
	print('Digite algo válido')
print('fim')
print(frase2 + 3.5)


while True:
	n = input('numero: ')
	
	if n.isnumeric():
		print('num')
		n = int(n)
	if n.is():
		print('dec')
'''

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



## --------------------------------------- ##