from eulerutil.prime import sieve

search = 6000
table = set(sieve(search))
sq = 100
constructed = set()
for i in range(1, sq + 1):
    for j in table:
        c = j + (2 * (i**2))
        if c % 2 == 1:
            constructed.add(c)

for i in range(3, search, 2):
    if i not in constructed and i not in table:
        print(i)
        break
