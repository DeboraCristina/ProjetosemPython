print()

print(f'{" DESAFIO 109 ":+^30}')

print()

from ex109 import moeda

val = float(input('Preço: '))

print(f'{moeda.moeda(val)} com 10% de aumento é {moeda.aumentar(val, 10, True)}.')

print(f'{moeda.moeda(val)} com 20% de desconto é {moeda.diminuir(val, 20,True)}.')

print(f'O dobro de {moeda.moeda(val)} é {moeda.dobro(val,True)}.')

print(f'A metade de {moeda.moeda(val)} é {moeda.metade(val)}.')

# moeda.