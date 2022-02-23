# monitorando o mouse

from pynput.mouse import Button, Listener

def click(x, y, button, pressed):
    print(x, y, button, pressed)
    if not pressed:
        return False

def move(x, y):
    print(x, y)

#listen = Listener(onc_lick = click, on_move = move, on_scroll = scroll)
#listen = Listener(on_click = click)
#listen.start()
#listen.join()
#listen.stop()

with Listener(on_click=click, on_move = move) as listen:
    listen.join()
