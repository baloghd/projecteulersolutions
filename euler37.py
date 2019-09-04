from eulerutil.prime import PrimeIterator, is_prime
from eulerutil.number_theory import numdigits

p = PrimeIterator(start = 10)
counter = 0

def truncateLeft(n: int) -> int:
    tento = 1
    while 10**(tento - 1) < n:
        yield n % 10**tento
        tento += 1
   
def truncateRight(n: int) -> int:
    tento = numdigits(n) - 1
    while tento > 0:
        yield n // 10**(tento)
        tento -= 1

n = next(p)
S = 0
while counter < 11 and n: 
	n = next(p)
	tl = truncateLeft(n)
	tr = truncateRight(n)

	tlg, trg = True, True

	try:
		while tl:
			t = next(tl)
			if not is_prime(t):
				tlg = False
				break
	except:
		pass

	try:

		while tr:
			t = next(tr)
			if not is_prime(t):
				trg = False
				break
	except:
		pass

	if tlg and trg:
		counter += 1
		print(f"found: {n}")
		S += n
print(S)