a, b = 1, 0
index = 1
while len(str(a)) != 1000:
    a, b = a + b, a
    index += 1
print (index)
