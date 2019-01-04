from eulerutil.combinatorics import choose

count = 0
# specification mentioned that the lower bound was 23
for i in range(23, 101):
    for j in range(1, i):
        if choose(i, j) > 1_000_000:
            count += 1
print(count)
