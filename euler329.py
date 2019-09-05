import random
from eulerutil.prime import is_prime, sieve

STEPS = 15
position = random.randint(1, 500)

seq = ""

for step in range(STEPS):
	if random.random() > 0.5:
		position += 1
	else:
		position -= 1

	if is_prime(position):
		if random.random() > 1/3:
			seq += "P"
		else:
			seq += "N"
	else:
		if random.random() > 2/3:
			seq += "P"
		else:
			seq += "N"

s = set(sieve(500))

n = 10_000
fc = 0
for i in range(n):
	if random.randint(1, 500) in s:
		fc += 1

print(fc/n)