from detecta_teclas import *

print('Tรก funcionando')

while True:
    ini()

    linha('oi', 'ola mundo')

    linha('aa', 'โ' )
    linha('as', 'โบ' )
    linha('la', '๐')
    linha('fim', '๐')
    
    seq('def','def func():', 0.2, Key.left, Key.left)
    seq('apm', Key.end, 0.2, Key.shift, Key.home, Key.backspace)

