from eulerutil.number_theory import *

known = dict()
for i in range(2, 1_000_000):
    seq = []
    n = i
    marlatotthossz = 0
    while n != 1:
        seq.append(int(n))
        if even(n):
            n /= 2
        else:
            n = 3*n + 1
        if n in known.keys():
            marlatotthossz = known[n]
            break
    known[i] = len(seq) + marlatotthossz
print(max(known, key = known.get))
