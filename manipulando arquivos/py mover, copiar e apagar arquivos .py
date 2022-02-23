
import os
import shutil

caminho_original = r'C:\Users\Débora\Desktop\organização\pasta01'
caminho_novo = r'C:\Users\Débora\Desktop\organização\pasta02'

try:
	os.mkdir(caminho_novo)
except FileExistsError as e:
	print('ja existi')
'''
for root, dir, files, in os.walk(caminho_original):
	for file in files:
		old_file_path = os.path.join(root, file)
		new_file_path = os.path.join(caminho_novo, file)
		
		## mover -> shutil.move(old_file_path, new_file_path)
		## copiar arquivos
		#if '.txt' in file:
		#	shutil.copy(old_file_path, new_file_path)
		#	print(f'{file} copiado com sucesso!')
		
		
		print(f'{file} copiado com sucesso!')
'''
## apagar arquivos

for root, dir, files, in os.walk(caminho_novo):
	for file in files:
		old_file_path = os.path.join(root, file)
		new_file_path = os.path.join(caminho_novo, file)
		
		if '.txt' in file:
			os.remove(new_file_path)
			print(f'{file} apagado com sucesso!')
