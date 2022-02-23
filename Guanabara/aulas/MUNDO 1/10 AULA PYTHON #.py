print ('Aula_10')
print ()
print ('-Condições-')
print('.Simple e Compostas.')
print ('#...')
# para cada situação coloca-se uma condição. ex: se um carro tem dois caminhos ele pode seguir ou o da direita ou o da esqueda. Se o ele seguir para esquedas seguira uma sequencia de comandos, se for para direita(se nao) ele seguira outra sequencia:
'''se carro.esqueda()
    bloco_v_ (verdadeiro)
senão (carro.direita())
    bloco_f_(falso)'''
#na estrutura condicional em Python
'''if carro.esqueda():
    blocoTrue
else:
    blocoFalse'''
# if para estruturas simples e else para estruturas compostas.
print('Exemplo: ')
tempo = int(input('Quantos ano tem seu carro: '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print ('FIM')
#condição simplificada
tempo = int(input('Quantos ano tem seu carro: '))
print('carro novo'if tempo<=3 else'carro velho')
print ('FIM')

print()

print('-Teste/Exemplos-')
nome = input('Qual é seu nome?: ')
if nome == 'Débora':
    print('Que nome maravilhoso! :)')
print('Bom dia, {}!'.format(nome))

print()

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2) / 2
print('A sua média é: {:.1f}.'.format(m)) 
if m >= 5:
	print('Vc foi Aprovado ;)')
else:
	print('Vc foi Reprovado ;(')