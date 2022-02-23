print('-_-_-EXERCICIOS 005 a 015-_-_-')

print()
#
z1 = 'sucerssor e antecessor'
z2 = 'dobro, triplo e raiz'
z3 = 'notas'
z4 = 'conversão de metros'
z5 = 'tabuada'
z6 = 'conversão de Dollar'
z7 = 'quantidade de tinta'
z8 = 'desconto'
z9 = 'aumento'
z10 = 'conversão de temperatura'
z11 = 'aluguel de Carros'
#


print('===== DESAFIO 05 =====')
print('{:_^40}'.format(z1))
 
#digitar um numero int, e mostrar seu sucerssor e antecessor.
print()
print('===== DESAFIO 06 =====')
print('{:_^40}'.format(z2))

#digitar um numero, e mostrar seu dobro, triplo e raiz quadrada.
print()
print('===== DESAFIO 07 =====')
print('{:_^40}'.format(z3))
 
#'ler' duas notas de um ALUNO e mostrar sua MÉDIA.
print()
print('===== DESAFIO 08 =====')
print('{:_^40}'.format(z4))
 
#'ler' um valor em metros e converte-lo em cm e mm
print()
print('===== DESAFIO 09 =====')
print('{:_^40}'.format(z5))

#digitar um numero int, e mostrar sua tabuada
print()
print('===== DESAFIO 10 =====')
print('{:_^40}'.format(z6))
 
#mostrar o quanto uma pessoa tem na carteira e converte-lo para dóllar
#us$=1 r$=5,32
print()
print('===== DESAFIO 11 =====')
print('===== DESAFIO JJ =====')
print('{:_^40}'.format(z7))
 
#ler largura e altura de uma parede em metros
#calcular area 
#e quantidade de tinta para pinta-la
#:1litro=2m**2:
print()
print('===== DESAFIO 12 =====')
print('{:_^40}'.format(z8))
 
#ler preço de um produto e dar 5% de desconto
print()
print('===== DESAFIO 13 =====')
print('{:_^40}'.format(z9))
 
#ler salario de um funcionario e dar 15% de aumento
print('===== DESAFIO 14 =====')
print('{:_^40}'.format(z1))
#converter celsius para fahrenheit (e kelvin)
print('===== DESAFIO 15 =====')
print('{:_^40}'.format(z1))
#ler km percorridos por um alugado e dias usados. E calcular o preço
#1dia=60R$ e 1km=0.15R$

print()

print(f'{"Resolução":+^20}')

print()

print('===== DESAFIO 05 =====')
a = int(input('Digite um Valor: '))
a1 = a - 1 #Antecessor
a2 = a +1 #Sucessor
print('Seu Antecessor é {}\ne seu Sucessor é {}'.format(a1,a2))

print()

print('===== DESAFIO 06 =====')
b = float(input('Digite um número: '))
b1 = b**(1/2) #Raiz
print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(b*2,b*3, b1))

print()

print('===== DESAFIO 07 =====')
c = input('Nome do Aluno: ')
c1 = float(input('Nota 01: '))
c2 = float(input('Nota 02: '))
c3 = (c1+c2)/2 #Média
print('Nome do Aluno: {};\n1º Semestre: {:.1f};\n2ºSemestre: {:.1f};\nNotaFinal: {:.1f}'.format(c, c1, c2, c3 ))

print()

print('===== DESAFIO 08 =====')
d = float(input('Metro: '))
dk = d / 1000 #Quilometro
dh = d / 100 #Hectometro
ddan = d / 10 #Decametro
ddm = d * 10 #Decimetros
dc = d * 100 #Centimetro
dmm = d * 1000 #Milimetro
print('Para{} metros são:\n{} km; {} hm; {} dam; \n{:.0f}dm; {:.0f} cm; {:.0f}mm'.format(d,dk,dh,ddan,ddm,dc,dmm))

print()

print('===== DESAFIO 09 =====')
e = int(input('Digite um Número: '))

#MINHA SOLUÇÃO
#print('{:=^16}'.format(''))
#print(e, 'x 01 = ', e*1)
#print(e, 'x 02 = ', e*2)
#print(e, 'x 03 = ', e*3)
#print(e, 'x 04 = ', e*4)
#print(e, 'x 05 = ', e*5)
#print(e, 'x 06 = ', e*6)
#print(e, 'x 07 = ', e*7)
#print(e, 'x 08 = ', e*8)
#print(e, 'x 09 = ', e*9)
#print(e, 'x 10 = ', e*10)
#print('{:=^16}'.format(''))

#MELHOR SOLUÇÃO
print('=' * 16)
print('{} x {:2} = {}'.format(e, 1, e * 1))
print('{} x {:2} = {}'.format(e, 2, e * 2))
print('{} x {:2} = {}'.format(e, 3, e * 3))
print('{} x {:2} = {}'.format(e, 4, e * 4))
print('{} x {:2} = {}'.format(e, 5, e * 5))
print('{} x {:2} = {}'.format(e, 6, e * 6))
print('{} x {:2} = {}'.format(e, 7, e * 7))
print('{} x {:2} = {}'.format(e, 8, e * 8))
print('{} x {:2} = {}'.format(e, 9, e * 9))
print('{} x {:2} = {}'.format(e,10, e * 10))
print('=' * 16)

print()

print('===== DESAFIO 10 =====')
f = float(input('Saldo: R$'))
f1 = 5.32 #Dollar em R$
f2 = 6.30 #Euro em R$
f3 = f/f1 #Saldo em Dollar
f4 = f/f3 #Salo em Euro
print('Com R${} você pode comprar US${:.2f} e {:.2f} euros.'.format(f, f3, f4))

print()

print('===== DESAFIO 11 =====')
ga = float(input('Altura, em Metros: '))
gl = float(input('Lagura, em Metros: '))
gar = ga*gl #Area
gqt = gar/2 #Quantidade de Tinta
print('Dimensão da Parede: {} x {} \nÁrea da Parede: {:.2f}m² \nQuantidade de Tinta: {:.2f} litros'.format(ga,gl,gar,gqt))

print()

print('===== DESAFIO 12 =====')
h = float(input('Preço: '))
h1 = h - (h * 0.05) #Desconto
print('Preço com Desconto de 5%: R$ {:.2f}'.format(h1))

print()

print('===== DESAFIO 13 =====')
i = float(input('Salario Atual: '))
i1 = i + (i * 0.15) #Aumento
print('Salario com Aumento: R$ {:.2f}'.format(i1))

print()

print('===== DESAFIO 14 =====')
j = float(input('Insira a Temperatura em °C: '))
j1 = (j * 1.8) + 32 #Fahrenheit
j2 = j + 273.15 #Kelvin
print('Convertendo {} °C temos: \n{} °F e {} K'.format(j,j1,j2))

print()

print('===== DESAFIO 15 =====')
kd = int(input('Insira quantos dias o veiculo foi usado: '))
kk = float(input('Insira quantos quilometros o veiculo foi usado: '))
k1 = (kd * 60) + (kk * 0.15)
print('O veiculo foi usado por {} dias e rodou {} km. \nO valor total a ser pago sera de R${:.2f}'.format(kd, kk, k1))

#CORRIGIDO#