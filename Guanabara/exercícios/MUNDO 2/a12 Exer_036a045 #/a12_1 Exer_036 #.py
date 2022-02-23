from time import sleep

print('===== DESAFIO 36 =====')

print()
print()
sleep(0.7)
print('{:^80}'.format('Para realizar o imprestimo, preencha os campos abaixo.'))
sleep(0.5)
print()

acasa = float(input('Insira o valor da casa: '))
sleep(0.5)
print()

asal = float(input('Insira seu salário: ')) * 0.3
sleep(0.5)
print()

ano = int(input('Em quantos anos pretende pagar: ')) * 12
sleep(0.5)
print()

acm = acasa / ano #valor mensal da casa

if acm > asal:
	print('Imprestimo negado.')
else:
	print('Imprestimo aprovado.')