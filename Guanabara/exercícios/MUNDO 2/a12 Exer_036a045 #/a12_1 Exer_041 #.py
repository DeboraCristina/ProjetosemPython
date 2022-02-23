print('===== DESAFIO 41 =====')

from datetime import date 
from time import sleep

print()

sleep(0.5)
idade = int(input("Insira seu ano de nascimento: "))
print()

idade = (date.today().year) - idade

sleep(0.4)
print('De acordo com a cofederação nacional de natação\nVocê é: ', end = '')
print()

if idade <= 9:
	print('mirim')
elif idade <= 14:
	print('infantil')
elif idade <= 19:
	print('junior')
elif idade <= 25:
	print('sênior')
elif idade > 25:
	print('master')