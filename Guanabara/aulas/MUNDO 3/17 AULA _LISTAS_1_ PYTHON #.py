print ('Aula_17')
print ()
print (F'{"-VARIÁVEIS COMPOSTAS-":^30}')
print (F'{"-Listas-":^30}')
print (F'{"-(PARTE 1)-":^30}')
print()
print('#...')
# Ao contrario das Tuplas, 
##		AS LISTAS SÃO MUTAVEIS		##
# Assim como as tuplas se caracterizam por () as listas se caracterizam por []
# O armazenamento das listas não se diferem do das tuplas.
'''
lanche = ['sorvete','suco','pizza','pudim']

lanche
|-------| |----| |-----| |-----|
|sorvete| |suco| |pizza| |pudim|
|-------| |----| |-----| |-----|
	0		1		2		3
'''

# se print(lanche[3])
'''
* PUDIM
'''
# se lanche[3] = torta

'''
lanche = ['sorvete','suco','pizza','torta']

lanche
|-------| |----| |-----| |-----|
|sorvete| |suco| |pizza| |torta|
|-------| |----| |-----| |-----|
	0		1		2		3
'''

# se print(lanche[3])
'''
* TORTA
'''

##### ADICIONAR ELEMENTOS A UMA LISTA #####

# Para adicionar algo a uma lista usa-se o metodo *.append*
# 'lanche.append('cookie')'
'''
lanche = ['sorvete', 'suco', 'pizza', 'torta', 'cookie']

lanche
|-------| |----| |-----| |-----| |------|
|sorvete| |suco| |pizza| |torta| |cookie|
|-------| |----| |-----| |-----| |------|
	0		1		2		3		4
'''

# Para adicionar um elemento em qualquer posição usa-se o metodo *.insert*
# 'lanche.insert(0, 'hotdog')'
'''
lanche = ['bolo', 'sorvete', 'suco', 'pizza', 'torta', 'cookie']

lanche
|----||-------||----||-----||-----||------|
|bolo||sorvete||suco||pizza||torta||cookie|
|----||-------||----||-----||-----||------|
   0	  1		 2		3		4		5
'''

##		 DELETAR ITENS DE LISTAS		 ##

# Para deletar algo de uma lista uma maneira é usando o comando *del*
# 'del lanche[3]'
# ou usando o metodo *.pop*, que geralmente elimina o último elemento mas pode-se passar um parametro a ser eliminado
# 'lanche.pop(3)'
# ou, ainda, o metodo *.remove*
# 'lanche.remove('pizza')'

# em todos os casos o elemento 3 vai ser eliminado....
'''
lanche = ['bolo', 'sorvete', 'suco', 'pizza', 'torta', 'cookie']

lanche
|----||-------||----||-----||-----||------|
|bolo||sorvete||suco||	   ||torta||cookie|
|----||-------||----||-----||-----||------|
   0	  1		 2		3		4		5
'''
# e a listas vai ser reorganizada.
'''
lanche = ['bolo', 'sorvete', 'suco', 'pizza', 'torta', 'cookie']

lanche
|----||-------||----||-----||------|
|bolo||sorvete||suco||torta||cookie|
|----||-------||----||-----||------|
   0	  1		 2		3		4
'''
# se 'lanche.pop()':
'''
lanche = ['bolo', 'sorvete', 'suco', 'pizza', 'torta', 'cookie']

lanche
|----||-------||----||-----|
|bolo||sorvete||suco||torta|
|----||-------||----||-----|
   0	  1		 2		3	
'''
## DECLARANDO E ORGANIZANDO LISTAS ##
# É possivel declarar uma lista a partir de um range:
# valores = list(range(4, 8))
'''
|---| |---| |---| |---|
| 4 | | 5 | | 6 | | 7 |
|---| |---| |---| |---|
  0     1     2     3
'''
print('...#')

print()

print(f'{"  Parte Prática  ":§^40}')

print()

num = [2, 5, 9, 1]
num[2] = 6
num.append(9)
num.insert(1, 7)
num.sort(reverse = True)
print(f'''
A lista :{num}
tem {len(num)} elementos
''')
dele = int(input('num: '))
if dele in num:
	num.remove(dele)
else:
	print('o numero pedido nao esta na lista.')
print(num)
num.pop()
print(num)

##      SORTED NÃO FUNCIONA EM LISTAS     ##

out = ['g', 'a', 'b']
print(out)
out.sort()
print(out)

n = [5, 3, 4, 8]
n.insert(3, 3)
print(n)
n.remove(3)
print(n)
# o *remove* só remove a 1ªocorrencia

#a = [1,2,3,4]
#b = a # ao igualar 2 listas, as 2 se ligam
#b[2] = 6
#print(f'''
#LISTA A: {a}
#LISTA B: {b}
#''')

#para copiar uma lista
a = [1,2,3,4]
b = a[:] # b recebe todos os elementos de a
b[2] = 6
print(f'''
LISTA A: {a}
LISTA B: {b}
''')
