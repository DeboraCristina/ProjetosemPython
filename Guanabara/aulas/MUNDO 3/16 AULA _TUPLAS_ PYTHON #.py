print ('Aula_16')
print ()
print (F'{"-VARIÁVEIS COMPOSTAS-":^30}')
print (F'{"-Tuplas-":^30}')
print()
print('#...')
# Qnd uma variavel é declarada ela cria uma espacinho na memoria. 
'''
	lanche
|------------|
|            |
|------------|

'''
#E para atribuir algo a essa variavel o sinal de '=' indica q ela recebe alguma coisa.
# ex: *lanche = hamburguer* (lanche recebe hamburguer)
'''
	lanche
|------------|
| hamburguer |
|------------|

'''
# se escrever *lanche = suco* na intenção de comer hamburguer com suco. o codigo vai na verdade subistituir o hamburguer pelo suco
'''
	lanche
|------------|
|    suco    |
|------------|

'''
# uma variavel simples nao consegue armazenar mais de um item.
# para criar uma variavel com mais espaços, um jeito são as tuplas.
# as tuplas podem armazenar quantos espaços (definidos) forem necessarios.
'''
				  lanche
|------------| |------------| |------------|
| hamburguer | |    suco    | |    pizza   |
|------------| |------------| |------------|

'''
# os espaços da tupla são identificados por indices.
'''
.				  lanche
|------------| |------------| |------------|
| hamburguer | |    suco    | |    pizza   |
|------------| |------------| |------------|
.		0			  1				 2
'''

# ----------fatiamento de tuplas---------- #

# as strings são exemplos de variaveis compostas.
# se escrever: *print(lanche)* o programa vai mostrar tudo q esta dentro de lanche.
# ja, se escrever: *print(lanche[2])* o programa vai mostrar "pizza".
# ja *print(lanche[0:2])* o programa vai mostrar "hamburguer" e "suco"

# ---tuplas em estruturas de repetição--- #

# se escrever: 
'''
for c in lanche:
	print(c)
print('acabou')
'''
# a cada vez "c", q é uma variavel simples, vai receber um item de lanche. E printar o q recebeu.
'''
+ hamburguer
+ suco
+ pizza
+ acabou
'''

##		## TUPLAS SÃO IMUTAVEIS ##		 ##
#uma vez definidas as tuplas são imutaveis#

print('...#')

print()

print(f'{"  Parte Prática  ":§^40}')

print()

# as variaveis compostas podem iniciar de tres formas
'''
com (), [] e {}.

(tuplas), [listas] e {dicionaarios}
'''

# para iniciar a tupla escreve - se o nome da variavel e ela recebe "()"

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

# as tuplas nao têm necessariamente de "()"

lanche = 'hamburguer', 'suco', 'pizza', 'pudim'

print('*' * 5, 'tupla inteira', '*' * 5)
print(lanche)
print()


print('*' * 5, 'tupla com fatiamento', '*' * 5)
print(lanche[0])
print()


##		##TUPLAS SÃO IMUTAVEIS##		##

'''
lanche.replace('pudim', 'casa')

print(lanche)
'''
# objetos tipo tupla nao suporta 'replace'

print('*' * 5, 'tupla em for', '*' * 5)
for comida in lanche:
	print(comida, end = ' ')
print()

print()
for p, c in enumerate(lanche):
	print(f'Vou querer o número {p}, que é o {c}')
print()

for cont in range(0, len(lanche)):
	print(f'Vou querer o número {cont}, que é o {lanche[cont]}')
print()

# "sorted" deixa a tupla em ordem

print(sorted(lanche))
print()

print('*' * 5, 'soma de tupla', '*' * 5)

a = 1, 5, 8
b = 9, 5, 7, 2
##c = a + b
# ao somar 2(ou +) tuplas. a tupla c simplesmente 'cola' uma tupla na outra.
c = b + a
#tanto que a ordem da soma tbm altera o resultado
print(c)

print(f'o tamanho de c é {len(c)}')
print(f'têm .{c.count(5)}. -5- em c')
print(f'a posição de 5 em c é {c.index(5)}')
print(f'a posição de 5 em c a partir da posição 2 é {c.index(5, 2)}')

'''
funciona tbm com letras

h = 'a', 'b', 'c'
i = 'd', 'e', 'f', 'g'
j = i + h
print(f'jota{j}')
'''

##	## TUPLAS SÓ RECEBEM TUPLAS ##	##

print('*' * 5, 'tuplas e tipos', '*' * 5)

pes = 'Débora', 17, 'F', 58.5
print(f'''
nome: {pes[0]}
idade: {pes[1]}
sexo: {pes[2]}
peso: {pes[3]}
''')

'''
k = 1
del(pes,k)
# o comando "del" deleta qualquer variavel.
print(pes, k)
del(pes[3])
# mas a tupla nao permite/suporta deltar um unico item 
'''
