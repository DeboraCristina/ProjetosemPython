

def teste():
	print('''
	moeda(1)
	aumentar(1, 2)
	diminuir(1, 2)
	dobro(1)
	metade(1)
	''')


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
		print(f"|{k:20}{v:>10}|")
	print("|" + "-" * 30 + "|")

