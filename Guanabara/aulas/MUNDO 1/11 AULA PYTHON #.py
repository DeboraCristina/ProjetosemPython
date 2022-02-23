print ('Aula_11')
print ()
print ('-Cores no Teminal-')
print('#...')
#uma das maneiras para 'colorir'. Um deles é o padrão ANSI
#tudo em ANSI começa com \ e um codigo.
# para começar um ANSI usa-se um \033[
#e o codigo é fechado com a letra 'm'
#\033[m

#detro do codigo tem o style; text; back
#				estilo; texto;background
#	  style; text; back
#\033[	   ;	 ;		m

#estilo: se vai estar em negrito, tamanho...
#texto: cor do texto
#background: cor de fundo
#NÃO IMPORTA A ORDEM	

#EX: \033[0;33;44m

#estilo
'''
0: nada
1: negrito
4: sublinhado
7: negativo
'''
#texto
'''
30: branco
31: vermelho
32: verde
33: amarelo
34: azul
35: roxo
36: ciano
37: cinza
'''
#background
'''
com as mesmas cores do texto
40
41
42
43
44
45
46
47
'''
print('...#')

print()

print('.Testes.')
#só funciona no pycharm
print('\033[30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[1;35;43mteste\033[m')
print('\033[7;32;41mteste\033[m')
print('\033[30mteste\033[m')
print('\033[7;30mteste\033[m')

a = 1
b = 2
print('os valores são \033[36m{}\033[m e \033[35m{}\033[m.'.format(a, b))

nome = 'Débora'
print('Olá, {}{}{}! Prazer em ti conhecer!'.format('\033[1;34m', nome, '\033[m'))
n = 'Débora'

#dicinario (só pra saber)
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'negativo': '\033[7;30m'}
print('Olá, {}{}{}! Prazer em ti conhecer!'.format(cores['negativo'], nome, cores['limpa']))