from eulerutil.number_theory import digits

inventory = dict()

def squarechain(n: int) -> int:
	collect = {n}
	while True:
		sqch = 0
		for d in digits(n):
			sqch += d**2
		if sqch in inventory.keys():
			for c in collect:
				inventory[c] = inventory[sqch]
			return
		if sqch == 1 or sqch == 89:
			for c in collect:
				inventory[c] = sqch
			return
		yield sqch
		n = sqch
		collect.add(n)

for n in range(2, 10_000_000):
	l = list(squarechain(n))

print(sum(i == 89 for i in inventory.values())