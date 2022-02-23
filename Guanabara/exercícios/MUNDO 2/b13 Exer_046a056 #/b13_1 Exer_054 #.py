print()

print(f'{" DESAFIO 54 ":+^30}')

print()


print(f'{" Por favor preencham a ficha abaixo ":#^50}')
print()

from datetime import date 

maior = 0
menor = 0

for c in range(0, 7):
	ano = int(input("Insira seu ano de nascimento: "))
	idade = date.today().year - ano
	print('O {}º participante tem {} anos'.format(c+1, idade))
	print()
	if idade >= 18:
		maior += 1
	else:
		menor += 1

print('Dentre os dados coletados, {} dos participantes do grupo são maiores de idade e {} dos participantes do grupo são menores de idade.'.format(maior, menor))