# saber as teclas
from pynput.keyboard import Controller, Key, Listener
from time import sleep

board = Controller()
ativo = False
conjunto = []
txt = ''

def press(key):
    print(key)

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
    if 'ctrl' in str(key):
        txt = str(conjunto[1:-1]).strip('[]').replace('\'', '').replace(', ', '')
        return False

def ini():
    with Listener(on_press = press, on_release = release) as listen:
        listen.join()

ini()

