from PySimpleGUI import PySimpleGUI as sg

thema = ['DarkTeal', 'DarkPurple1']
font = ('Arial', '12')

# Layout
sg.theme(thema[0])
layou1 = [
    [sg.Text(f'Textinho fofo',justification='center',size=(15, 1), font = font, text_color = '#000')],
    [sg.Input(key = 'input', size = (15, 1))],
    [sg.Button('botao')]
]
layou2 = [
    [sg.Text(f'Textinho fofo',justification='center',size=(15, 1), font = font, text_color = '#000')],
    [sg.Input(key = 'input', size = (15, 1))],
    [sg.Button('botao')]
]

# Janela
janela1 = sg.Window('Teste1', layou1, size = (200, 50))
janela2 = sg.Window('Teste2', layou2, size = (200, 50))

# Ler Eventos
while True:
    eventos, valores = janela1.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'botao':
        print(valores['input'])

while True:
    eventos, valores = janela2.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'botao':
        print(valores['input'])
