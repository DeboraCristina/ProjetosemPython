print ('Aula_21')
print ()
print (F'{"-FUNÇÕES-":^30}')
print (F'{"-PARTE 2-":^30}')
print()

def Teoria(t = 'x'):
	if t in 'Ii':
		print()
		print('#...')
	elif t in 'fF':
		print('...#')
		print()
		
def Prática():
	print()

	print(f'{"  Parte Prática  ":§^40}')

	print()

Teoria('i')

###            TÓPICOS DA AULA            ###
'''
° Interactive Help
° docstrings
° Argumentos opcionais
° Escopo de variáveis
° Retorno de resultados
'''

## INTERACTIVE HELP

# Para ter ajuda em python basta usar a função 'help()'
'''
help()
help(print)
'''
# Outra maneira é printar o '.__doc__' de uma função.
'''
print(len.__doc__)
'''

###            DOCSTRINGS            ###

# As docstrings são basicamente um manual de uma função
# EX: (em uma função criada pode-se colocar uma docstring/manual dentro dela)
'''
def contador(i, f, p):
	"""
	
	-> Mostra uma contagem na tela.
	:param i: Início da contagem
	:param f: Fim da contagem
	:param p: Passo da contagem
	:return: Sem retorno
	Funcao mt util
	"""
	for c in range(i, f + 1, p):
		print(c, end = ' → ')
	print('Fim')

contador(0, 10, 2)
help(contador)
'''

###         PARÂMETROS OPCIONAIS          ###

# Enquanto os ''Multipos Parâmetros'' funcionariam basicamente assim:
'''
def soma(a, b, c):
	s = a + b + c
	print(f'A soma vale {s}.')
soma(3, 2, 5)
'''
# onde a chamada abaixo daria ERRO
'''
soma(8, 4)
'''
# Os os Parâmetros opcionais já funcionariam assim:
'''
def soma(a = 0, b = 0, c = 0):
	"""
	Faz a soma de 3 valores.
	:param a: Primeiro valor
	:param b: Segundo valor
	:param c: Terceiro valor
	"""
	s = a + b + c
	print(f'A soma vale {s}.')
# Onde todos (ou alguns) valores são de Preenchimento opcional.
soma(3, 5, 2)
soma(8, 4)
soma()
help(soma)
'''

###         ESCOPO DE VARIÁVEIS         ###
# EX1:
'''
def teste():
	x = 8 # 'x' tem um -escopo local-, ou seja, só é válida dentro de 'teste'
	print(f'Na função teste n vale {n}.')
	print(f'Na função teste x vale {x}.')


n = 2 # 'n' tem -escopo global-, pois é válida em qualquer chamada após sua declaração.
print(f'No programa Principal n vale {n}.')
print(f'No programa Principal x vale {x}.')

teste()
'''
# EX2:
'''
def teste(b):
	a = 8 # esse 'a' é uma v.local
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 5 #enquanto esse é uma v.global
teste(a)
print(f'A fora vale {a}')
'''
# os espaços na memória
'''
## local
  |-|   |-|   |-|
a |8| b |9| c |2|
  |-|   |-|   |-|
## global
  |-|
a |8|
  |-|
'''

'''
def teste(b):
	global a # agr declarando q 'a' é global
	a = 8 # esse 'a' é uma v.global, modificando o original.
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 5 
teste(a)
print(f'A fora vale {a}')
'''
# os espaços na memória
'''
## local
  |-|   |-|
b |9| c |2|
  |-|   |-|
## global
  |-|
a |8|
  |-|
'''

## RETORNO DE VALORES ##
# A função abaixo além de imutavél ao longo do código não retorna o valor de 's'.
'''
def fsoma(a = 0, b = 0, c = 0):
	s = a + b + c
	print(f'A soma vale {s}.')

fsoma(10, 4, 6)
'''
# Já com o retorno de 's' abre-se um leque de possibilidades.
'''
def soma(a = 0, b = 0, c = 0):
	s = a + b + c
	return s

n1 = 5
n2 = 9
n3 = 1

m = soma(n1, n2, n3) / 3

print(f'A média é {m}')
'''
Teoria('f')

Prática()

def fac(num = 1):
	f = 1
	for c in range(num, 0, -1):
		f *= c
	return f

n = 2
print(f'O fatorial de {n} é {fac(n)}.')

def pi(n = 0):
	if n % 2 == 0:
		return True
	else:
		return False

num = int(input('Número: '))

print(pi(num))

