

def moeda(n = 0):
	m = f"R${n:.2f}".replace('.', ',')
	return m


def aumentar(n = 0, pa = 0):
	au = n + (n * (pa / 100))
	return au


def diminuir(n = 0, pd = 0):
	di = n - (n * (pd / 100))
	return di


def dobro(n = 0):
	d = n * 2
	return d


def metade(n = 0):
	m = n / 2
	return m

