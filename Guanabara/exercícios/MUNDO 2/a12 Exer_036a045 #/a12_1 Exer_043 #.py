print()
from stringcolor import cs

print(f'{"Calculo de IMC":-^40}')

print()

print('Insira a sua altura. \n(sem ponto ou vígula)')
altura = str(input(': '))
qa = len(altura)
altura = float(altura)

if qa == 1:
	altura = altura
elif qa == 2:
	altura = altura / 10
elif qa == 3:
	altura = altura / 100
elif qa >= 4:
	altura = 'erro'

print()

print('Insira a seu peso. \n(sem ponto ou vígula)')
peso = str(input(': '))
qp = len(peso)
peso = float(peso)

if qp <= 2:
	peso = peso
elif qp == 3:
	peso = peso / 10
elif qp >= 4:
	peso = peso / 100
elif qp > 5:
	peso = 'erro'

if peso == 'erro' or altura == 'erro':
	imc = 'erro'
else:
	imc = peso / (altura**2)

if imc == 'erro':
	resultado = ('Erro! Alguma iformação está incorreta.')
elif imc < 18.5:
	resultado = ('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
	resultado = ('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
	resultado = ('Você é acima do peso ideal.')
elif imc >= 30 and imc < 40:
	resultado = ('Você está a nível de obesidade.')
elif imc > 40:
	resultado = ('Você está a nível de obesidade móbida.')

print()

print('''Com {}m de altura e pesando {}kg seu Índice de Massa Corpórea é {:.1f}.
{}'''.format(altura, peso, imc, resultado))

#pycharm
'''
if imc == 'erro':
	resultado = cs('Erro! Alguma iformação está incorreta.', "rgb(170,0,0)")
elif imc < 18.5:
	resultado = cs('Você está abaixo do peso ideal.', "rgb(0,255,200)")
elif imc >= 18.5 and imc < 25:
	resultado = cs('Você está no peso ideal.', "rgb(0,200,255)")
elif imc >= 25 and imc < 30:
	resultado = cs('Você é acima do peso ideal.', "rgb(255,0,255)")
elif imc >= 30 and imc < 40:
	resultado = cs('Você está a nível de obesidade.', "rgb(255,0,0)")
elif imc > 40:
	resultado = (cs('Você está a nível de obesidade móbida.', "rgb(255, 170, 0)"))

print()

print('Com {}m de altura e pesando {}kg seu Índice de Massa Corpórea é {:.2f}.\n{}'.format(altura, peso, imc, resultado))
'''