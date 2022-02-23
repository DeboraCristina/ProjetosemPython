import os

meu_caminho = input("digite um caminho: ")

path = r'{}'.format(meu_caminho)
#path = r'C:\Users\Débora\Programas\AutoHotkey\HotKeys'
term = input('digite o termo: ')

for raiz, dir, arquivos in os.walk(path):
	for arquivo in arquivos:
		if term in arquivo:
			caminho = os.path.join(raiz, arquivo)
			nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
			tamanho = os.path.getsize(caminho)
			
			print("")
			print('''achei o arquivo: {}
Caminho: {}
Nome: {}
Extensão: {}
Tamanho: {}
'''.format(arquivo, caminho, nome_arquivo, ext_arquivo, tamanho))

print('fim')
