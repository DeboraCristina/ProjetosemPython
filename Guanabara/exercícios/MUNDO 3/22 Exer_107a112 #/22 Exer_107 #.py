print()

print(f'{" DESAFIO 107 ":+^30}')

print()

from ex107 import moeda

val = float(input('Diga o preço: R$'))

print()

print(f'R${val} com 10% de aumento é R${moeda.aumentar(val, 10)}.')
print(f'R${val} com 20% de desconto é R${moeda.diminuir(val, 20)}.')
print(f'O dobro de R${val} é R${moeda.dobro(val)}.')
print(f'A metade de R${val} é R${moeda.metade(val)}.')
