from eulerutil.combinatorics import Pascal_triangle

count = 0
# specification mentioned that the lower bound was 23
for i in range(23, 101):
    count += len(list(filter(lambda x: x > 1_000_000, Pascal_triangle(i))))
print(count)
