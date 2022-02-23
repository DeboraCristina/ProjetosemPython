print('===== DESAFIO 37 =====')

from time import sleep

print()

sleep(0.7)
print('{:^50}'.format(':Conversor de Valores:'))
print()
sleep(0.5)

num = int(input('Insira um número: '))
print(
'''
{ 1 } Hexadecimal
{ 2 } Binário
{ 3 } Octal
'''
)
sleep(0.5)

con = int(input('Escola a base de Conversão: '))

print()

#minha solução
if con == 1:
	print('O número {} em Hexadecimal é {}.'.format(num, str(hex(num)).replace('0x', '')))
	
elif con == 2:
	print('O número {} em Binário é {}.'.format(num, str(bin(num)).replace('0b', '')))
	
elif con == 3:
	print('O número {} em Octal é {}.'.format(num, str(oct(num)).replace('0o', '')))
#outra solução
'''
if con == 1:
	print('O número {} em Hexadecimal é {}.'.format(num, str(hex(num)[2:])))
	
elif con == 2:
	print('O número {} em Binário é {}.'.format(num, str(bin(num)[2:])))
	
elif con == 3:
	print('O número {} em Octal é {}.'.format(num, str(oct(num)[2:])))
'''

else:
	print('Escola um opção válida.')