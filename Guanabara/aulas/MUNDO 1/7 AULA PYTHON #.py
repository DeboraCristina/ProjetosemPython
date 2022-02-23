print ('Aula_7')
print ()
print('-Operadores Aritméticos-')
print('#...')
#Há vários operadores
# SOMA +
# SUBTRAÇÃO -
# MULTIPLICAÇÃO *
# DIVISÃO / (NUMERO COM DECIMAL)
# POTENCIA **
# DIVISÃO_INTEIRA // (NUMERO INTEIRO)
# RESTO_DA_DIVISÃO % 

#Ordem de Precedência
# Expressões Numéricas - ()
    # Python não se usa [] nem {}, só ()
# 1º ()
# 2º **
# 3º * / // %
# 4º + -
print()
print('...#')

print()

print('-Operadores com String-')
a = 5
print('5 + (5**2) =', a+(a**2))
print('oi * 5 =', "oi "*a)

print()

print('-Operações, Chaves e Melhorando o Print-')
b1 = '.Em String.'
print('{:^40}'.format(b1))
b = input('Digite seu Nome: ')
print('OLÁ, {:20}! Prazer em te conhecer!'.format(b))
#{:x}).format - escreve B em x espaços
print('OLÁ, {:^20}! Prazer em te conhecer!'.format(b))
#{:^x}).format 
# ^ cetraliza B
# > alinha à direita
# < alinha à esquerda
print('OLÁ, {:+^20}! Prazer em te conhecer!'.format(b))
#qualquer sinal entre : e o alinhador preenche os espaços vazios com ele


b2 = '.Em Int.'
print('{:^39}'.format(b2))
c1 = int(input('valor01: '))
c2 = int(input('valor02: '))
cso = c1 + c2
csu = c1 - c2
cm = c1 * c2
cd = c1 / c2
cdi = c1 // c2
cp = c1 ** c2
print('A Soma é: {}, A Diferença é: {} e O Produto é {}.'.format(cso, csu, cm))
print('A Divisão é {:.2f}, A Divisão Inteira é {} e A Exponenciasão é {}.'.format(cd, cdi, cp))

print()

#Para não haver quebra de linha de um PRINT para outro, usa-se um "end = '' "
print('A Soma é: {}, A Diferença é: {} e O Produto é {}.'.format(cso, csu, cm), end = ' ')
print('A Divisão é {:.2f}, A Divisão Inteira é {} e A Exponenciasão é {}.'.format(cd, cdi, cp))

print()

#Para o contrario usa-se \n
print('A Soma é: {},\n A Diferença é: {}\n e O Produto é {}.'.format(cso, csu, cm), )
print('A Divisão é {:.2f},\n A Divisão Inteira é {}\n e A Exponenciasão é {}.'.format(cd, cdi, cp))