import os
from playwright.sync_api import sync_playwright
from PySimpleGUI import PySimpleGUI as sg
from subprocess import run

#pegar o link. (arquivo a ser aberto pelo navegador)
protocolo = 'file://'
caminho = os.getcwd()
arquivos = os.listdir(caminho)

for arquivo in arquivos:
    if '.html' in arquivo:
        caminho = f'{protocolo}{caminho}/{arquivo}'
        break

#eventos e ações
evento = [
    'Reload',
    'Clear',
    'Close'
]

#Peças pra UI
tema = 'DarkPurple1'
fonte = ('Arial', '12')
cor = '#fff'
sg.theme(tema)
lay = [
    [sg.Text(f'Recarregar Pagina', justification='center',size=(15, 1), font=fonte, text_color = cor)],
    [sg.Button(evento[0]), sg.Button(evento[1])],
    [sg.Button(evento[2])]
]
jan = sg.Window('Opções', lay)

print('teste')
print('teste')
print('teste')
print('teste')
print('teste')

with sync_playwright() as p:
#abrir a janela
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(caminho)
    while True:
        e, v = jan.read()
        if e == sg.WIN_CLOSED:
            jan.close()
            break
        if e == evento[0]:
            page.reload()
        elif e == evento[1]:
            run(['clear'])
        elif e == evento[2]:
            jan.close()
            break
    browser.close()


