from math import sqrt
from eulerutil.number_theory import whole

pentagonal_test = lambda x: whole((sqrt(24*x + 1) + 1) / 6)
hexagonal_test = lambda x: whole((sqrt(8*x + 1) + 1) / 4)

ti = 286
while True:
    if pentagonal_test(ti * (ti + 1) / 2) and hexagonal_test(ti * (ti + 1) / 2):
        break
    ti += 1
    
print(int(ti * (ti + 1) / 2))
    
    
