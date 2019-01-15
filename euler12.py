from eulerutil.number_theory import *
from eulerutil.prime import *

from functools import reduce

n = 1
while True:
    t = (n * (n + 1))//2
    n_even = n % 2 == 0
    if n_even:
        p = prime_factors(n//2) + prime_factors(n+1)
        #print(prime_factors(n//2)+ prime_factors(n+1), t)
    else:
        p = prime_factors(n) + prime_factors((n+1)//2)
        #print(prime_factors(n) +prime_factors((n+1)//2), t)
    d = reduce(lambda x, y: x * y, map(lambda x: x + 1, p.values()))
    #print(d)
    if d > 500:
        break
    n += 1
print(n, t)

#summa = 0
#s = 3
#for n in range(1, 1000):
    #summa += numdivisors(n)/(n**s)

