print('===== DESAFIO 39 =====')

print()

from datetime import date
from time import sleep

sleep(0.5)
idade = int(input('Digite o ano em que você nasceu: '))
print()
ano = (date.today().year)
idade = ano - idade

sleep(0.5)
print(f'Você tem {idade} anos.')

print()

if idade < 18:
	saldo = 18 - idade
	print('Ainda falta {} anos para seu alistamento. Seu alistamento será em {}.'.format(saldo, ano + saldo))

elif idade == 18:
	print('Já está na hora do seu alistamento.')

else:
	saldo = idade - 18
	print('Você está {} anos trasado para seu alistamento. Deveria ter se alistado em {}'.format(saldo, ano - saldo))
