# controlando mouse

from pynput.mouse import Button, Controller

mouse = Controller()
## seta a posição absoluta do mouse
#mouse.position = (720, 100)

## seta a posição relativa do mouse
#mouse.move(-100, 0)

## clica com o mouse, 1ºparam=botão 2ºparam=quantidade de clickes
#mouse.click(Button.left, 2)

## preciona um botão (não larga)
#mouse.press(Button.left)
## solta o botão
#mouse.release(Button.left)

## scroll do mouse
#mouse.scroll(100, 0)
