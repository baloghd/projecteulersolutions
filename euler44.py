penta2 = lambda x: x * (3*x - 1) / 2
set_of_pentas = set(penta2(i) for i in range(1, 10001))
D = lambda j, k: int(abs(penta2(j) - penta2(k)))

for a in range(1, 2500):
    for k in range(2, 2500):
        if a <= k:
            pa, pk = penta2(a), penta2(k)
            if abs((pa - pk)) in set_of_pentas and (pa + pk) in set_of_pentas:
                print("megvan", a, k, D(a, k))
                break
