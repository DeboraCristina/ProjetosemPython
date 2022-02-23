print ('Aula_8')
print ()
print ('-Trabalhando com Módulos-')
print('#...')
# os programas basicos em python vêm com poucos "pacotes" para adicionar mais usase o comando 'import'.
# tendo como exemplos as bibliotecas: doces e bebidas. Podemos importalas pelo comando import+bebidas
#ex: import bebidas
# o comando acima importa todos os itens. mas si eu quiser importar apenas um item como o brigadeiro
#ex: from doces import brigadeiro

#import math 
#from math import sqrt
print('...#')

print('{:^30}'.format('importando tudo em math'))
import math
num = int(input('numero: '))
raiz = math.sqrt(num )
print('A raiz de {} é {}.'.format(num, math.ceil(raiz)))

print('{:^30}'.format('importando só a raiz em math'))
from math import sqrt
nume = int(input('numero: '))
ra = sqrt(nume )
print('A raiz de {} é {:.2f}.'.format(nume,ra))