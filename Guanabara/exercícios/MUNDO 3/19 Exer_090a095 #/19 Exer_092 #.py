print()

print(f'{" DESAFIO 92 ":+^30}')

print()

from datetime import date

pessoa = {}

pessoa['Nome'] = input('Digite seu nome: ')
print()

ano = (date.today().year)
pessoa['Idade'] = ano - int(input('Digite o ano em que nasceu: '))
print()

pessoa['N° da Cateira'] = int(input('Número da Cateira de Trabalho: '))
print()

if pessoa['N° da Cateira'] != 0:
	
	pessoa['Salário'] = float(input('Qual seu Salário? '))
	print()
	
	pessoa['Ano de Contratação'] = int(input('Em que ano foi a contratação? '))
	print()
	
	pessoa['Aposentadoria'] = pessoa['Idade'] + ( 35 - (ano - pessoa['Ano de Contratação']))
	
	if pessoa['Idade'] >= pessoa['Aposentadoria']:
		pessoa['Status'] = 'Já Pode se Aposentar'
	else:
		pessoa['Status'] = 'Não Pode se Aposentar ainda'

print()

for c, i in pessoa.items():
	if c == 'Idade' or c == 'Aposentadoria':
		print(f'{c} é {i} anos')
	else:
		print(f'{c} é {i}')
	print()
