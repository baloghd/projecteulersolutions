from eulerutil.number_theory import *

n = 1

while True:
    t = (n * (n + 1))//2
    n_even = n % 2 == 0
    if n_even:
        p = numdivisors(n//2) * numdivisors(n+1)
    else:
        p = numdivisors(n) * numdivisors((n+1)//2)
    if p > 500:
        break
    n += 1
print(n, t)
