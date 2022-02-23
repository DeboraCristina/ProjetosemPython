print ('Aula_13')
print ()
print ('-Laços de Repetição-')
print('ou Laço com variavel de controle')
print()
print('#...')
#ao inves de escrever a msm estrutura divesas vezes usamos um laço
#o laço ira se repetir por determinadas vezes

#pensando em um caminho
''' passo, passo, passo, ...'''
#laçocnoIntevalo(1, 10)
#	passo
#pega
#em python
#forcinrange(1, 10):
#passo
#pega

#pensando em um caminho com buracos
''' passo, pula, passo, pula, passo, pula, ...'''
#laçocnoIntevalo(0, 3)
#	passo 
#	pula
#passo
#pega
#forcinrange(0, 3)
#	passo
#	pula
#passo
#pega

#pensando em um caminho com buracos e moedas
''' passo, pula, pega, passo, pula, pega, passo, pula, pega, ...'''
#laçocnoIntevalo(0, 3)
#	se tiver moeda
#		pega
#	passo 
#	pula
#passo
#pega
#forcinrange(0, 3)
#	if moeda == True
#		pega
#	passo
#	pula
#passo
#pega

# o for para a repetição no ultimo número
print('...#')

print()

print('testes')
print()

#mostra oq está dentro da estrutura quantas vezes for pedido
for c in range(1, 5):
	print('oi')
print('fim')
print()

#mostra a contagem de numeros pedido
for c in range(0,6):
	print(c)
print()

#para uma contagem contraria se diz ao laço qual a interação
#                     |          
for c in range(6, 0, -1):
	print(c)
print()

#pula de 2 em 2
for c in range(0, 10, 2):
	print(c)
print()

n = int(input('Insira um número: '))
#entre "for" e "in" pode-se inserir qualquer str. conta como variavel.
# "c" não é uma estrutura fixa
for h in range(0, n+1):
	print(h)
print('FIM')
print()

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for a in range(i, f+1, p):
	print(a)
print('FIM')
print()

s = 0
for c in range(0, 4):
	n = int(input('digite um número: '))
	s += n
print(s)