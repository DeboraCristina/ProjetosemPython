#primeiro jeito
'''
file = open("abc.txt", "w+")
file.write("linha1\n")
file.write("linha2\n")
file.write("linha3\n")

file.seek(0, 0)
print("lendo linha: ")
print(file.read())

print()
print("{:-<40}".format(''))
print("")

file.seek(0)
print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline())

print()
print("{:-<40}".format(''))
print("")

file.seek(0, 0)
for linha in file:
	print(linha, end="")

file.close()
'''
#ou
'''
with open("abc.txt", "w+") as file:
	file.write("linha1\n")
	file.write("linha2\n")
	file.write("linha3\n")

	file.seek(0, 0)
	print("lendo linha: ")
	print(file.read())

	print()
	print("{:-<40}".format(''))
	print("")

	file.seek(0)
	print(file.readline(), end = "")
	print(file.readline(), end = "")
	print(file.readline())

	print()
	print("{:-<40}".format(''))
	print("")

	file.seek(0, 0)
	for linha in file:
		print(linha, end="")
'''
#modos open:
''' o "+" faz o modo mais o "read" '''
## w - 'write'
'''
with open('abc.txt', "w+") as escreve:
	escreve.write("linha1\n")
	escreve.write("linha2\n")
	escreve.write("linha3\n")
	
	escreve.seek(0)
	print(escreve.read())
'''

## r - "read"
'''
with open('abc.txt', 'r') as leia:
	print(leia.read())
'''

## a - append
'''
with open('abc.txt', "a+") as add:
	add.write("ola mundo!\n")
	
	add.seek(0)
	print(add.read())
'''


## ler linhas especificas
'''
with open("abc.txt") as fp:
    for i, line in enumerate(fp):
        if i == 0:
            pontuação = str(line)
        elif i == 5:
            pass
        elif i > 8:
            break
'''

## escrever linhas especificas
'''
pontos = 3

novo = open("abc.txt", 'r')
novo_names = novo.readlines()
novo_names[3] = str(pontos) + '\n'

novo = open("abc.txt", 'w')
novo.writelines(novo_names)
novo.close()
'''

'''
try:
    file = open('apps//datas.txt', 'x')
except:
    label01.setText('ja exist')
'''