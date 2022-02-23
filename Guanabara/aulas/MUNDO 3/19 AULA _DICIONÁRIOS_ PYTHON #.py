print ('Aula_19')
print ()
print (F'{"-VARIÁVEIS COMPOSTAS-":^30}')
print (F'{"-Dicionários-":^30}')
print()
print('#...')
# dados = list()
'''
dados
|-------|
|		|
|-------|
'''
# dados.append('Pedro')
'''
dados
|-------|
| Pedro |
|-------|
	0
'''
# dados.append(25)
'''
dados
|-------| |----|
| Pedro | | 25 |
|-------| |----|
	0		1
'''
# print(dados[0]) → *Pedro
# print(dados[1]) → *25

# Seria mais facil se um item nome estivesse em um indece 'NOMES'. Em dicionários isso é possivel.
## Para declarar um dicionários usa-se {}
# dados = dict()
# dados = {'nome': 'Pedro', 'idade': 25}
'''
dados
|-------| |----|
| Pedro | | 25 |
|-------| |----|
  nome    idade
'''
# print(dados['nome']) → *Pedro
# print(dados['idade']) → *25

## PARA ADICIONAR ITENS EM UM DICIONÁRIO ##
# dados['sexo'] = M
'''
dados
|-------| |----| |---|
| Pedro | | 25 | | M |
|-------| |----| |---|
  nome    idade  sexo
'''

## PARA REMOVER ITENS EM UM DICIONÁRIO ##
# del dados['idade']
'''
dados
|-------| |---|
| Pedro | | M |
|-------| |---|
  nome     sexo
'''
filme = {
'titulo': 'Star Wars', 
'ano': 1977, 
'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

# Essas informações podem ser usadas em laços
for k, v in filme.items():
	print(f'O {k} é {v}')

print('...#')

print()

print(f'{"  Parte Prática  ":§^40}')

print()

pessoas = {'nome': 'Gustavo', 'idade': 22, 'sexo': 'M'}
print('O' if pessoas["sexo"] == 'M' else 'A', f'{pessoas["nome"]} tem {pessoas["idade"]} anos')

# Enquanto nas Tupla e Listas usava-se o 'enumerate' nos dicionários usa-se o '.items()'
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
	print(f'{k} = {v}')
	
estado = {}
brasil = []
for c in range(0, 3):
	estado['uf'] = input('Unidade Federativa: ')
	estado['sigla'] = input('Sigla do Estado: ')
	brasil.append(estado.copy())
print(brasil)

