from eulerutil.combinatorics import factorial
from eulerutil.number_theory import digits

digitfacts = {i: factorial(i) for i in range(10)}

summa = 0
for i in range(3,100000):
    if i == sum([digitfacts[digit] for digit in digits(i)]):
        summa += i
print(summa)
