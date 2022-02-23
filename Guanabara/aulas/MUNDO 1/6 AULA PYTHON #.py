print('AULA_6')

print()

print('para fazer comentarios nos scripts Python, se coloca um #')
# comentario

print()

chaves = ('chaves{}')
formato = ('.format')
print('Para melhorar as mensagens no PRINT, usamos as {}'.format(chaves),'em seguida um {}'.format(formato))

print()

print('- Tipos_Primitivos -')
print('Há 4 Tipos Primitivos Principais')
print('.1º Tipo -> int.')
print('DESAFIO 3')
print('r era igual a a+b -> ab')
print('O TP int concerta isso')
a = int(input('1º Termo: '))
b = int (input('2º Termo: '))
r = a + b
print('A Soma é ', r)

print()

print('Os 4 Tipos são:')
print('1º.int - 2º.float - 3º. bool - 4º.str')
print('int : números inteiros. 7 ou -3')
print('float : números reais. 4.5 ou 0.04')
print('bool : valores boleanos. True e False')
print('str : strings. como ','"ola"')

print()

print('Teste 1')
print('n1 = input("Digite o valor: ") = "str"')
print('n1 = int(input("Digite o valor: "")) = "int"')
print('print(type(n1)) = tipo do valor')
n1 = int(input('Digite o valor: '))
n2 = int(input('Digite Outro: '))
print('A soma é: {}'.format(n1+n2))
print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))

print()

print('Teste 2')
m = float(input('Digite um valor float: '))
print('',m)
d = bool(input('Digite um valor: '))
print('',d)
e = input('Digite um algo: ')
print(e.isnumeric())
print('O Metodo "is" diz se os caracteres da "variavel" é o que foi perguntado.')