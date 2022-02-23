print()

print(f'{" DESAFIO 112 ":+^30}')

print()

from ex112.dados import moeda

while True:
    val = input('Preço: ').strip()

    moeda.resumo(val, 50, 40)
