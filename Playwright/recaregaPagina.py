from PySimpleGUI import PySimpleGUI as sg
from playwright.sync_api import sync_playwright
from subprocess import run

def txt(psg, txt, just=None, tam=(None, None), fonte=None, cor=None):
    return psg.Text(f'{txt}', justification=just, size=tam, font=fonte, text_color=cor)
def btn(psg, txt, tam=(None, None)):
    return psg.Button(f'{txt}', size = tam)
def inp(psg, key, txt=None, tam=(None, None)):
    return psg.Input(txt, key = key, size=tam)

thema = ['DarkTeal', 'DarkPurple1']
font = ('Arial', '12')

# Layout
sg.theme(thema[1])

lay01 = [
    [txt(sg, 'Pagina'), inp(sg, key='url')],
    [btn(sg, 'submit', (20,1))],
]

lay02 = [
    [sg.Text(f'Recarregar Pagina', justification='center',size=(15, 1), font = font, text_color = '#000')],
    [sg.Button('recarregar'), btn(sg, 'clear')],
    [sg.Button('close')],
]

# Janela
jan1 = sg.Window('Site', lay01, size=(200, 70))
jan2 = sg.Window('Recarregar', lay02)

# Ler Eventos
site = ''

while True:
    e, v=jan1.read()
    if e == sg.WIN_CLOSED:
        jan1.close()
        break
    if e == 'submit':
        if v['url'] != '':
            site = v['url']
            jan1.close()
            break

if site != '':
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto(site)
        while True:
            eventos, valores = jan2.read()
            page.on("console", lambda msg: print(msg.text))
            if eventos == sg.WIN_CLOSED:
                jan2.close()
                break
            if eventos == 'recarregar':
                page.reload()
            if eventos == 'close':
                browser.close()
                jan2.close()
                break
            if eventos == 'clear':
                run(['clear'])
