from eulerutil.prime import is_prime

seeked_prime = 0
i, count = 2, 0
while True:
    if is_prime(i):
        seeked_prime = i
        count += 1
    if count == 10001:
        break
    i += 1

print(seeked_prime)
    
