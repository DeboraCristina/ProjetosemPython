print('===== DESAFIO 40 =====')

from time import sleep
print()

sleep(0.5)
n1 = float(input('Isira a 1ª nota: '))
print()

sleep(0.5)
n2 = float(input('Isira a 2ª nota: '))
print()

media = (n1 + n2) / 2

sleep(0.5)
if media < 5:
	print('Sua média é de {:.1f}. Você reprovou.'.format(media))
elif 7 > media >= 5 :
	print('Sua média é de {:.1f}. Você está de recuperação.'.format(media))
else:
	print('Sua média é de {:.1f}. Você foi aprovado.'.format(media))