print('-_-_-EXERCICIOS 022 a 027-_-_-')

print()

print('===== DESAFIO 22 =====')

'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas. 
- Quantas letras ao todo (sem considerar espaços). 
- Quantas letras tem o primeiro nome.'''

print()

print('===== DESAFIO 23 =====')

'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
ex: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''

print()

print('===== DESAFIO 24 =====')

#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print()

print('===== DESAFIO 25 =====')

#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print()

print('===== DESAFIO 26 =====')

'''Faça um programa que leia uma frase pelo teclado e mostre 
-quantas vezes aparece a letra "A" 
-em que posição ela aparece a primeira vez 
-em que posição ela aparece a última vez.'''

print()

print('===== DESAFIO 27 =====')

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print()

print(f'{"RESOLUÇÃO":+^30}')

print()

print('===== DESAFIO 22 =====')
a = input('Insira seu Nome Completo: ').strip()
am1 = a.upper() #letra maiuscula
am2 = a.lower() #letra minuscula
al = len(a)-a.count(' ')#todas as letra
a1l = len(a.split()[0][0:])#letra 1ª palavra
#'a1l = len(a.find(' '))#letra 1ª palavra'
print('O nome {} \nem letras totalmente minusculas fica: {} \nem letras maiusculas fica: {}.\no nome {} tem {} letras e {} tem {} letras.'.format(a, am2, am1, a, al, a.split()[0],a1l))

print('===== DESAFIO 23 =====')
b = int(input('Insira um Número: ')).strip().replace(' ','')
b = '{:0>4}'.format(b)
#uma boa solução
#b = input('Insira um Número: ').strip().zfill(4)
b1 = (b[3]) #Unidade
b2 = (b[2]) #Dezena
b3 = (b[1]) #Centena
b4 = (b[0]) #Milhar
print('''Unidade: {:3}
Dezena: {:3}
Centena: {:3}
Milhar: {:3}'''.format(b1,b2,b3,b4))

print('===== DESAFIO 24 =====')
'''c = input('Insira um Nome de uma cidade: ').strip()
c = c.title
c2 = c.upper().split()
c1 = 'SANTO' in c2[0]
print('A palavra {} tem a palavra Santo?\n: {}.'.format(c,c1))'''
#Melhor solução
cid = input('Insira um Nome de uma cidade: ').strip ()
print(cid[:5].upper() == 'SANTO')

print('===== DESAFIO 25 =====')
d = input('Insiraseu Nome Completo: ').strip()
d1 = 'SILVA' in d.upper()
print('O nome SILVA está no nome {}?\n: {}'.format(d.title(),d1))

print('===== DESAFIO 26 =====')
e = input('Insira uma Frase: ').strip().upper()
ev = e.count('A')
epp = e.find('A') + 1
epu = e.rfind('A') +1
print('''Na Frase '{}' tem
{} letras A;
A primeira vez que 'A' aparece é na posição {};
E a última vez que 'A' aparece é na posição {}.'''.format(e.title(),ev, epp, epu))

print('===== DESAFIO 27 =====')
f = input('Insira seu Nome Conpleto: ').strip().title().split()
f1 = f[0]
f2 = f[len(f) - 1]
print('Primeiro Nome: {};\nUltimo Nome: {}.'.format(f1, f2))
#CORRIGIDO#