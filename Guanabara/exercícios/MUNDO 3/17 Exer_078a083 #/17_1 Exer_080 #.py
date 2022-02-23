print()

print(f'{" DESAFIO 80 ":+^30}')

print()

l = []

for c in range(0,5):
	n = int(input('Número: '))
	if c == 0 or n > l[-1]:
		l.append(n)
	else:
		p = 0
		while p < len(l):
			if n <= l[p]:
				l.insert(p, n)
				break
			p += 1
print(l)