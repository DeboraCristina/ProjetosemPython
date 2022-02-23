print()

print(f'{" DESAFIO 106 ":+^30}')

print()

from stringcolor import cs, name, bold

def frase(txt = '', ct = 'black', cf = 'white', doc = False):

	if txt != '':
		if doc == False:
			tam = len(txt) + 6
			print(cs('→' * tam, ct, cf))
			print(cs(' ' * tam, ct, cf))
			
			print(f'{cs("   ", ct, cf)}{cs(txt, ct, cf).bold()}{cs("   ", ct, cf)}')

			print(cs(' ' * tam, ct, cf))
			print(cs('→' * tam, ct, cf))
		else:
			lis = f'As Informações sobre a função →{txt}← são: '
			tam = len(lis) + 6
			print(cs('←' * tam, ct, cf))
			print(cs(' ' * tam, ct, cf))
			
			print(f'{cs("   ", ct, cf)}{cs(lis, ct, cf).bold()}{cs("   ", ct, cf)}')
			
			print(cs(' ' * tam, ct, cf))
			print(cs('←' * tam, ct, cf))
			print()

			h = str(help(txt)).replace("None", "")

			#print(f'{cs(h, ct, cf)}')

	else:
		print()

while True:
	
	frase('SISTEMA HELP PYTHON', 'magenta', 'blue')
	
	frase()
	
	resp = input(cs('Help >>','blue').bold()).strip().lower()
	
	if resp == 'sair':
		break
	
	frase()
	
	frase(resp, 'pink', 'darkgreen', doc = True)
	
	frase()

# nao tem como pintar o help
'''
from stringcolor import cs, bold
    
    c = {'azul': 'blue',
        'vermelho': 'red',
        'verde': 'green',
        'ciano': 'cyan2',
        'magenta': 'magenta',
        'amarelo': 'yellow2',
        'rosa': 'deeppink7',
        'vermelhobad': 'maroon',
        'branco': 'black',
        'preto': 'white',
        'manu': '\033[7;30m',
        'nada': '\033[m'
         }
    
    
    def ajuda(com):
        tit(f'Manula do comando \'{com}\'', 'branco', 'verde')
        print(c['manu'], end = '')
        help(com)
        print(c['nada'])
    
    
    def tit(msg, ct = 'branco', cf = 'preto'):
        tam = len(msg) + 4
        m = f'  {msg}  '
    
        print(cs('-' * tam, c[ct], c[cf]))
        print(cs(m, c[ct], c[cf]).bold())
        print(cs('-' * tam, c[ct], c[cf]))
    
    
    # prog
    
    while True:
        tit('SISTEMA DE AJUDA', 'amarelo', 'preto')
        comando = input(cs('help >> ', 'blue').bold()).lower().strip()
        if comando == 'sair':
            break
        else:
            ajuda(comando)
    tit('ATÉ LOGO', 'amarelo', 'preto')
'''