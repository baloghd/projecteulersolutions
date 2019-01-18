def palindromic(n: int or str) -> bool:
    s = str(n)
    for index, char in enumerate(s):
        if index + 1 <= len(s)//2:
            if s[index] != s[-(index + 1)]:
                return False
    return True

acc = 0
for i in range(1_000_000):
    if palindromic(i) and palindromic(bin(i)[2:]):
       acc += i
