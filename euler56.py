from eulerutil.number_theory import sumdigits

N = [i ** j for i in range(100) for j in range(100)]

N = list(map(sumdigits, N))

print(max(N))