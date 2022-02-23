print()

print(f'{" DESAFIO 73 ":+^30}')

print()

clubes = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense', 'Bahia', 'Sport', 'Corinthians', 'Fortaleza', 'Ceará', 'Atlético-GO', 'Bragantino', 'Vasco', 'Athletico-PR', 'Coritiba', 'Botafogo', 'Goiás')
print(f'''Os *cinco* Primeiros colocados são: 

{clubes[0]}
{clubes[1]}
{clubes[2]}
{clubes[3]}
{clubes[4]}
{clubes[0:5]}
''')
print(f'''Os *quatro* últimos colocados são:

{clubes[-1]}
{clubes[-2]}
{clubes[-3]}
{clubes[-4]}
{clubes[-4:]}
''')
print('Os times em ordem alfabética são:')
for n in sorted(clubes):
	print(n, end = ' ')
print()
print()

if clubes.count('Chapecoense') <= 0:
	print('O time Chapecoense não foi classificado.')
else:
	chap = clubes.index('Chapecoense')
	print(f'O time Chapecoense está na posição {chap+1}ª.')
print()