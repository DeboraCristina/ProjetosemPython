print()

print(f'{" DESAFIO 91 ":+^30}')

print()

from random import randint

'''
jogo = {}
joji = []

for c in range(0, 4):
	n = randint(1, 6)
	jogo['Jogador ' + str(c + 1)] = n
	joji.append(n)

joji.sort(reverse = True)

for c in range(0, 4):
	for 

print(jogo)
'''

resutados = dict()

jogadores = list()

print('Valores sorteados:')

for c in range(0, 4):

    n = randint(1, 6)

    resutados['Jogador'+str(c+1)] = n

    jogadores.append(n)



    print(f'O {"Jogador"+str(c+1)} tirou {n}')

jogadores.sort(reverse= True)

jogar = 't'

print('Ranking dos jogadores:')

for p in range(0,4):

    print(f'{p+1}º Lugar: ', end='')

    for k, v in resutados.items():

        if v == jogadores[p] and jogar != k:

            

            print(k,'com',v)

            jogar = k

            break