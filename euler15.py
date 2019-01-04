from eulerutil.combinatorics import choose

# https://math.stackexchange.com/questions/636128/calculating-the-number-of-possible-paths-through-some-squares

# 20 steps down, 20 steps to the right
# -> (20 + 20) choose 20 = 137846528820

print(choose(40, 20))
