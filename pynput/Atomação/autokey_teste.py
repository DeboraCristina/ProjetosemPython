from detecta_teclas import *

print('Tá funcionando')

while True:
    ini()

    linha('oi', 'ola mundo')

    linha('aa', '→' )
    linha('as', '►' )
    linha('la', '👉')
    linha('fim', '🏁')
    
    seq('def','def func():', 0.2, Key.left, Key.left)
    seq('apm', Key.end, 0.2, Key.shift, Key.home, Key.backspace)

