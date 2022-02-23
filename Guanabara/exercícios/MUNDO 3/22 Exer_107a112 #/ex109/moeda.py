

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

	return au if mo is False else moeda(au)


def diminuir(n, pd, mo = False):
	di = n - (n * (pd / 100))

	return di if not mo else moeda(di)


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

