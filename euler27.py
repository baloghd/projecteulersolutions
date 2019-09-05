import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from eulerutil.prime import is_prime

def countPrimes(a: int, b: int) -> int:
	n = 0
	count = 0
	while True:
		number = n ** 2 + a * n + b
		if not is_prime(number):
			return count
		else:
			count += 1
		n += 1

data = []
max_cP = 0
A, B = 0, 0
for a in range(-1000, 1000):
	for b in range(-1000, 1001):
		cP = countPrimes(a, b)
		if cP > max_cP:
			max_cP = cP
			A = a
			B = b
print(max_cP, A*B)