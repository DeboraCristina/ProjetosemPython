print ('Aula_22')
print ()
print (F'{"-MÓDUDO E PACOTES-":^30}')
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

## Modularização serve para criação de módulos ##
# Foco: dividir um programa grande
# Foco: aumentar a legibilidade
# Foco: facilita manutenção

'''
def fatorial(n):
	f = 1
	for c in range(n, 1, -1):
		f *= c
	return f


def dobro(n):
	return n * 2


def triplo(n):
	return n * 3


num = int(input('didite um valor: '))
fac = fatorial(num)
print(f'O fatorial de {num} é {fac}.')
'''
# digamos q o código acima comece a ficar confuso
# para resolver isso cria-se o arquivo uteis.py
# pois todo arquivo .py é potencialmete um módulo


'''
		uteis.py
|----------------------------|
|def fatorial(n):            |
|	f = 1                    |
|	for c in range(n, 1, -1):|
|		f *= c               |
|	return f                 |
|                            |
|                            |
|def dobro(n):               |
|	return n * 2             |
|                            |
|                            |
|def triplo(n):              |
|	return n * 3             |
|----------------------------|
'''

# agora, importando 'uteis' o código fica menor.
'''
from uteis import *

num = int(input('didite um valor: '))
fac = fatorial(num)
print(f'O fatorial de {num} é {fac}.')
'''
## PACOTES ##
# caso os módulos estejam sobre carregados
# pode-se criar os pacotes
# Para criar um pacote basta criar uma pasta 

# pois, assim como, todo arquivo .py é potencialmete um módulo, toda pasta é potencialmete um pacote

from uteis import num

num.help()
n = num.dobro(7)

print(n)

# ao criar um pacote

Teoria('f')