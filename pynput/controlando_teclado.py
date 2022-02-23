# Controlando teclado

from time import sleep
from pynput.keyboard import Key, Controller

keyb = Controller()

## precionar uma tecla alphanumerica
#keyb.press('d')
## soltar uma tecla alphanumerica
#keyb.release('d')

## digitar um texto
#keyb.type('ola mundo!')

## precionar uma tecla não-alphanumerica
#keyb.press(Key.cmd)
#keyb.relase(Key.cmd)

## precionar um conjuto de teclas (hotkey)
'''
with keyb.pressed(Key.ctrl):
    keyb.press('l')
    keyb.release('l')
'''

def tecle(s, t):
    keyb.press(t)
    sleep(s)
    keyb.release(t)

tecle(0.2, Key.backspace)
