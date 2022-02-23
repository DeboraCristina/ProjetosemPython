print ('Aula_9')
print ()
print ('-Manipulando Textos-')

print ('#...')
#Uma Frase 'CursoemVideo'
#para o python é 'uma cadeia de caracteres' ou um 'string'
frase = 'Curso em Video'
#para o python a string é armazenada assim:
# C u r s o _ e m _ V i d e o
#sendo que cade caractere recebe um indice 
# C u r s o _ e m _ V  i  d  e  o
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13

#com essa configuração pode-se fazer algumas operações. Como:
print ('fatiamento: ')
print (frase[9])
# O [9] irá selecionar o caractere de numero 9, no caso a letra V
print (frase[9:14])
# O [9:13] irá selecionar os caracteres de 9 a 13, no caso: Vide
print (frase[9:14:2])
# O :2 faz com que seja escrita palavra pulando de 2 em 2 caracteres
print(frase[:5])
# :5 é o mesmo q 0:5
print(frase[9:])
# 9: é o mesmo q 9:14
print (frase[9::3])
# 9::3 é o mesmo q [9:14:2]
print ('análise: ')
print (len(frase))
# len() mostra o comprimento da string + 1
print (frase.count('o'))
# count() mostra quantos 'o' (minusculos) têm na string.
print (frase.count('o', 0, 13))
# count('x', 0, 13) mostra quantos 'o' (minusculos) têm na string do caractere 0 ao 12. [análise+fatiamento]
print (frase.find('deo'))
# find('deo') mostra onde começa 'deo' na string. 'deo' começa no indice 11.
print (frase.find('Android'))
# quando se coloca um string não existente no .find() ele dá resultato -1. Ou seja, ele não achou a palavra na string.
print ('Curso' in frase)
# pergunta se existe 'Curso' em frase. Se sim: True. Se não: False.
print ('Transformação: ')
#Por padrão não se pode mudar uma lista de string. Mas atraves de metodos podemos muda-la.
print (frase.replace('Video', 'Android'))
#replace vai trocar a palavra Vide pela palavra Android. Sem mudar a string original.
print (frase.upper())
#upper muda todas os caracteres minusculos para maiusculos.
print (frase.lower())
#lower muda todas os caracteres maiusculos para minusculos.
print (frase.capitalize())
#capitalize deixa apenas a Primeria letra da string em maiuscula. Sem deferenciar a quantidade de palavras.
print (frase.title())
#title vai deferenciar a quantidade de palavras, contando os espaços, e deixando a Primeria letra de cada palavra em maiuscula.

frase2 = '   Aprenda Python  '
# _ _ _ A p r e n d a _ P y t h o n _ _
# 0 - 18 indices

print (frase2.strip())
#strip remove os espaços inuteis no começo e no fim da string. O caractere 'A' que antes tinha o indice 3 passa a ter o indice 0.
print (frase2.rstrip())
#o 'r' faz com que o strip remova só os espaços da direita.
print (frase2.lstrip())
#e o 'l' faz com que o strip remova só os espaços da esquerda.

# 'l' e 'r' podem 'alterar' varios módulos. 'l' left e 'r' right

print ('Divisão: ')
print (frase.split())
#split cria uma divisão onde houver espaços. Criando 'outras strings'/'outras lista'. 
#cada palavra ganha uma nova indiciação: 
#e cada lista tambem ganha uma numeração:
# C u r s o   e m   V i d e o
# 0 1 2 3 4   0 1   0 1 2 3 4
#  1           2     3 ("elementos")
print ('Junção: ')
print ('-'.join(frase.split()))
#join(frase.split()) substitue os espaços por '-'
#join sozinho separa cada caracter com um '-'

print ('..#')

print ('teste')

print('''Pode ser que um dia não mais existamos.
Mas, se ainda sobrar amizade,
nasceremos de novo um para o outro.''')
#imprime um texto inteiro

print(frase.upper().count('O'))
#o python deferencia letras maiusculas de minusculas. entao sem o upper o count mostraria 0, mas como a 'frase' foi comvertida para letras em maiusculas ele deu um resultado 2.
print(len(frase2))
print(len(frase2.strip()))

'''frase3 = 'Curse em Video Python'
frase3.replace('Python', 'Android')
print(frase3)'''
#o python vai imprimir a 'frase3' original, pois 'frase3.replace('Python', 'Android')' esta apenas em uma instancia(não esta salvo)
#mas se:
frase3 = 'Curso em Video Python'
print(frase3)
frase3 = frase3.replace('Python', 'Android')
print(frase3)
#a frase foi mudada

dividido = frase3.split()
print(dividido[2][3])
#"me mostre a frase 'dividido', palavra 2, a 3ª letra"