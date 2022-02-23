print('Aula_23')
print()
print(F'{"-TRATAMENTO DE ERROS-":^30}')
print()


def Teoria(t='x'):
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
# Um erro comum é o erro de sintaxe
'''
priMt(x)
'''
# erro semantico (NameError)
'''
print(x)
'''
# erro de valor
## se for digitado um valor q, no caso, nao seja inteiro.
'''
n = int(input('Número: '))
'''

# erro de diviisao por 0(zero)
'''
a = int(input("Numerador: "))
b = int(input('Denominador: '))
r = a/b
print(f'{a} dividido por {b} é {r}')
'''

# erro de tipo (TypeError)
'''
r = 2/'2'
'''

# erro de IndexError
'''
lis = [1, 2, 3]
print(lis[3])
'''
# ou KeyError
'''
dic = {'a':1,'b': 2,'c': 3}
print(dic['e'])
'''

# error de modulo nao encontrado
'''
import uteis
'''

# Existem MUITAS exceções no Python
# mas com o comando try
'''
try:
    *operação
except:
    *se falhar
else: (opcional)
    *se der certo
finally:  (opcional)
    *se der ou nao certo
'''

Teoria('f')

Prática()

from stringcolor import *

'''try:
    #a = int(input('Numerador: '))
    a = 'r'
    b = int(input("Denominador: "))
    r = a/b


except Exception as erro:
    error = str(erro.__class__).replace('class ', '').replace('\'', '').replace('<', '').replace('>', '')
    print(cs(f'Houve um problema de {error}', 'cyan').bold())

else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!!')'''

try:
    a = int(input('Numerador: '))
    b = int(input("Denominador: "))
    r = a/b

except ZeroDivisionError:
    print('nao da pra dividir por zero')

except Exception as erro:
    print(f'Houve um erro de {erro.__class__}')

else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre!!')

