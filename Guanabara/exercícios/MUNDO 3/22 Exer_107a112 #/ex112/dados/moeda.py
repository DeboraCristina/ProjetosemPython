

def teste():
	print('''
	moeda(1)
	aumentar(1, 2)
	diminuir(1, 2)
	dobro(1)
	metade(1)
	''')


def numero(n):
	'''
	input de um número inteiro ou decimal
	: txt: texto dentro do input
	(EX: input(txt))
	: t: tipo de valor:
	i para int
	f para float	
	'''
	
	if n == '':
		return 00
		
		
	num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
			
	erro = False
	f = []
			
	for l in n:
		if l == '.' or l == ',':
			f.append(l)
		if l not in num:
			erro = True
	if len(f) > 1:
		erro = True
			
	if erro:
		return 00
	else:
		if ',' in n:
				n = float(n.replace(',', '.'))
		return float(n)
	


def moeda(n):
	m = f"{n:.2f}"
	m = f"R${m.replace('.', ',')}"
	return m


def aumentar(n, pa, mo = False):
	au = n + (n * (pa / 100))
	
	if mo:
		au = moeda(au)
	return au


def diminuir(n, pd, mo = False):
	di = n - (n * (pd / 100))
	
	if mo:
		di = moeda(di)
	return di


def dobro(n, mo = False):
	d = n * 2
	
	if mo:
		d = moeda(d)
	return d


def metade(n, mo = False):
	me = n / 2
	
	if mo:
		me = moeda(me)
	return me


def resumo(n, pa = 1, pd = 1):
	from stringcolor import cs
	if numero(n) != 00:
		n = numero(n)
		res = {}
		res['Preço:'] = moeda(n)
		res['Dobro:'] = dobro(n, True)
		res['Metade:'] = metade(n, True)
		res[f'{pa}% de Aumento:'] = aumentar(n, pa, True)
		res[f'{pd}% de Disconto:'] = diminuir(n, pd, True)
		
		print("|" + "-" * 30 + "|")
		print(f"|{'RESUMO DO PREÇO':^30}|")
		print("|" + "-" * 30 + "|")
		for k, v in res.items():
			print(f"|{k:20}{v:<10}|")
		print("|" + "-" * 30 + "|")
	else:
		print(cs('Digite algo válido.', 'red').bold())

