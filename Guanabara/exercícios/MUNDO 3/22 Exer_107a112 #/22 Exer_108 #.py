print()

print(f'{" DESAFIO 108 ":+^30}')

print()

from ex108 import moeda

val = float(input('Preço: '))

print(f'{moeda.moeda(val)} com 10% de aumento é {moeda.moeda(moeda.aumentar(val, 10))}.')
print(f'{moeda.moeda(val)} com 20% de desconto é {moeda.moeda(moeda.diminuir(val, 20))}.')
print(f'O dobro de {moeda.moeda(val)} é {moeda.moeda(moeda.dobro(val))}.')
print(f'A metade de {moeda.moeda(val)} é {moeda.moeda(moeda.metade(val))}.')
# moeda.moeda()