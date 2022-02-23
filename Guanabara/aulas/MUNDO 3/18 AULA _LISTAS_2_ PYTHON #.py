print ('Aula_18')
print ()
print (F'{"-VARIÁVEIS COMPOSTAS-":^30}')
print (F'{"-Listas-":^30}')
print (F'{"-(PARTE 2)-":^30}')
print()
print('#...')
# Para adicionar uma estrutura na outra pode-se:
# dados = ['pedro', 25]
'''
dados
|=======|==|
|'pedro'|25|
|=======|==|
'''
# pessoas = []
# pessoas.append(dados[:])
'''
pessoas
/============/============/============/
/|=======|==|/|=======|==|/|=======|==|/
/|'pedro'|25|/|'maria'|19|/|' joao'|32|/
/|=======|==|/|=======|==|/|=======|==|/
/============/============/============/
	0				1			2
'''
# Para declarar toda essa estrutura direto:
# pessoas = [['pedro', 25], ['maria', 19], ['joao', 32]]
# se print(pessoas[0][0])
'''
+ pedro
'''

# se print(pessoas[1][1])
'''
+19
'''

# se print(pessoas[2][0])
'''
+joao
'''

# se print(pessoas[1])
'''
+['maria', 19]
'''
print('...#')

print()

print(f'{"  Parte Prática  ":§^40}')

print()

teste = []
teste += ['Débora']
teste.append(34)
galera = []
galera.append(teste[:])
teste[0] = 'jorge'
teste[1] = 18
galera.append(teste[:])
print(galera)

galera = [['Vitoria', 20], ['Luis', 40], ['Gilda', 16]]
print(f'''
A galera: {galera}
A galera[0]: {galera[0][0]} com {galera[0][1]} anos
Tamanho da galera: {len(galera)}
''')
print(galera.index(['Vitoria', 20]))

galera = []
dados = []

for c in range(0, 5):
	dados.append(str(input('Nome: ')))
	dados.append(int(input('Idade: ')))
	galera.append(dados[:])
	dados.clear()

for d in galera:
	print(f'{d[0]:.<15}{d[1]}')
		