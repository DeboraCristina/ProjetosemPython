from pynput.keyboard import Controller, Key, Listener
from time import sleep

board = Controller()
ativo = False
conjunto = []
txt = ''

## detectar teclas
def press(key):
    #print(key)
    pass

def release(key):
    global ativo, conjunto, txt
    #entrada
    if 'shift' in str(key):
        print('digite a hotkey:')
        ativo = True
        conjunto.clear()
    # adiciona
    if ativo:
        conjunto.append(key)
    # saída
    if 'space' in str(key):
        txt = str(conjunto[1:-1]).strip('[]').replace('\'', '').replace(', ', '')
        return False

def ini():
    with Listener(on_press = press, on_release = release) as listen:
        listen.join()

##

# escrever uma linha de acordo com abreviação 
def linha(a, b):
    global txt
    if txt == a:
        for l in range(0, len(txt)+1):
            board.press(Key.backspace)
            board.release(Key.backspace)
        board.type(b)

## "instruções"
# escrever linha
def escreva(texto):
    board.type(texto)

#teclar determinada tecla
def tecle(t):
    board.press(t)
    board.release(t)

def seq(*seq):
    global txt
    if seq[0] == txt:
        for l in range(0, len(txt)+1):
            board.press(Key.backspace)
            board.release(Key.backspace)
        for i in seq:
            if i != seq[0]:
                if type(i) == float or type(i) == int:
                    sleep(i) #esperar um tempo
                elif 'shift' in str(i):
                    board.press(Key.shift)
                elif type(i) != str:
                    tecle(i) #teclar teclas
                else:
                    escreva(i) #escrever algo
        board.release(Key.shift)


'''
print(f'Você digitou o comando {txt}')
    
if txt == 'oi':
    board.type('ola mundo')
'''

