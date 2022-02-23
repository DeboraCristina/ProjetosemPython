print('-_-_-EXERCICIOS 003 e 004-_-_-')

print('===== DESAFIO 03(03) =====')
# Refazer o DESAFIO 03
a1 = float(input('1º Termo: '))
a2 = float(input('2º Termo: '))
a3 = a1 + a2
print('A Soma entre {} e {} é: {}'.format(a1, a2, a3))

print()

print('===== DESAFIO 04 =====')
b1 = input('Insira um Algo:')
#type isss
print()
print('O Tipo Primitivo do Valor é {}'.format(type(b1)))
print('O Valor é numérico? :', b1.isnumeric())
print('O Valor é alfabético? :', b1.isalpha())
print('O Valor é um dígito? :', b1.isdigit())
print('O Valor é alfanumérico? :', b1.isalnum())
print('O Valor está em MAIÚSCULAS?:', b1.isupper())
print('O Valor está em mininúsculas?:', b1.islower())
print('O Valor está Capitalizada?:', b1.istitle())

#corrigido#