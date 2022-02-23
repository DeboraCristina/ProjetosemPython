import os

'''#dir is not keyword
newpath = r'olha ela' 
if not os.path.exists(newpath):
    os.makedirs(newpath)'''
#dir is not keyword
newpath = input('Qual o nome da pasta? ') 
if not os.path.exists(newpath):
    os.makedirs(newpath)