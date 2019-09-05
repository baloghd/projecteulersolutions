import random

LIMIT = 10_000
S = 0

for i in range(LIMIT):
	n = 0
	c = 0
	while n != 2**32 - 1:
		n |= random.randint(0, 2**32)
		c += 1
	S += c

print(S / LIMIT)