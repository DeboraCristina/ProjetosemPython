print()

print(f'{" DESAFIO 101 ":+^30}')

print()

def voto(a):
	from datetime import date
	
	anoatual = date.today().year

	idade = anoatual - a
	
	if idade < 16:
		v = 'Não vota'
	elif 60 > idade >= 18:
		v = 'Voto obrigatório'
	elif idade >= 60 or idade >= 16:
		v = 'Voto opcional'
	else:
		v = 'ERRO'
	print(f'Com {idade} anos: {v}.')

ano = int(input('Ano de nascimento: '))

voto(ano)