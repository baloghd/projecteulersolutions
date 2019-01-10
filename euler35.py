from eulerutil.number_theory import digits
from eulerutil.prime import is_prime

cprimedigits = [1, 3, 7, 9]

count = 13
for i in range(100, 1_000_000):
    if (i % 10) % 2 == 1 and (i % 10) != 5:
        if not any([False if n in cprimedigits else True for n in digits(i)]):
            if is_prime(i):
                d = digits(i)[::-1]
                circular = True
                nn = len(d) 
                for j in range(nn):
                    d = [d.pop()] + d[:(nn - 1)]
                    if not is_prime(int("".join(map(str, d)))):
                        circular = False
                        break
                if circular:
                    print(i)
                    count += 1
print(count)
