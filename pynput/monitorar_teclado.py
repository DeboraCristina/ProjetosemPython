# monitorar teclado

from pynput.keyboard import Listener, Key

def press(key):
    print(key)

def release(key):
    '''
    if key == Key.shift:
        return False
    '''
    if 'shift' in str(key):
        return False

with Listener(on_press = press, on_release = release) as listen:
    listen.join()


