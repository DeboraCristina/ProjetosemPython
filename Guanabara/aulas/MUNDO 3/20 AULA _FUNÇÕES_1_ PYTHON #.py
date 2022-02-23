print ('Aula_20')
print ()
print (F'{"-FUNÇÕES-":^30}')
print (F'{"-PARTE 1-":^30}')
print()

def Teoria():
	print('...#...')
def Prática():
	print()

	print(f'{"  Parte Prática  ":§^40}')

	print()


Teoria()
## O QUE É ##
# Funções estão vinculadas a uma 'rotina'.
# Algo q se faz com frequência.
# EX
'''
print()
len()
int()
'''

## CRIAR FUNÇÕES ##

# Pode-se criar uma função de, por exemplo, 'mostraLinha()', com o comando 'def'.
'''
-----------------
'''

'''
----------------
	SISTEMA
----------------
----------------
	CADASTRO
----------------
----------------
	FORMULA
----------------
'''
# Para fazer o texte acima ficaria um código repetitivo
print('----------------')
print('    SISTEMA')
print('----------------')

print('----------------')
print('    CADASTRO')
print('----------------')

print('----------------')
print('    FORMULA')
print('----------------')

# Para criar uma função/rotina. usa-se o comando 'def'.
def mostraLinha():
	print('----------------')
# todas a funções em Python terminam com '()'.

# agora o código ficará:
mostraLinha()
print('    SISTEMA')
mostraLinha()

mostraLinha()
print('    CADASTRO')
mostraLinha()

mostraLinha()
print('    FORMULA')
mostraLinha()
# A cada vez q se executa o 'mostraLinha()' ele aciona o 'def' q por sua vez executa oq está dentro do bloco.

## PARÂMETROS ##
# Nas linhas abaixo há um padrão:
'''
print('----------------')
print('    SISTEMA')
print('----------------')

print('----------------')
print('    CADASTRO')
print('----------------')

print('----------------')
print('    FORMULA')
print('----------------')
'''
# As linhas abaixo se repetem 3 vez. Mudando apenas o miolo da 2ª linha.
'''
print('----------------')
print('    ')
print('----------------')
'''
#
def mensagem(msg):
	print('----------------')
	print(f'{msg:^16}')
	print('----------------')

mensagem('SISTEMA')
mensagem('CADASTRO')
mensagem('FORMULÁRIO')

## EMPACOTAMENTO DE PARÂMETROS ##
# Em situações onde não se sabe a quantidade de parâmetros, usa-se '*', pois '*' mostra para o Python q não há um número exato de parâmetros.
# Todos os parâmetros passados serão jogados na tupla declarada.
def contador(*num):
	print(num)
	
	tam = len(num)
	print(tam)

contador(2, 4, 6, 8)
contador(4, 7, 2, 0, 6)

def dobra(lis):
	pos = 0
	while pos < len(lis):
		lis[pos] *= 2
		pos += 1

valores = [2, 4, 5]
dobra(valores)
print(valores)

Teoria()

Prática()

'''
a = 4
b = 5
c = a + b
print(c)

a = 4
b = 5
c = a + b
print(c)

a = 4
b = 5
c = a + b
print(c)
'''

def soma(a, b):
	c = a + b
	print(c)


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a = 6, b = 4)
soma(b = 5, a = 3)

def som(*val):
	s = 0
	for n in val:
		s += n
	print(s)

som(5, 2)
som(9, 4, 2)