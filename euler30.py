from eulerutil.number_theory import digits

d5th = {i:i**5 for i in range(0, 10)}

def digitToSum(n: int) -> int:
    return sum([d5th[i] for i in digits(n)])

s = 0
for i in range(1000, 200000):
    d = digitToSum(i)
    if i >= d:
        if i == d:
            s += i
            #print(i, d)
print(s)
