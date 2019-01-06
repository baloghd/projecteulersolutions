codes = [line.strip() for line in open('euler79_keylog.txt')]
s = set("".join(codes))
after = dict(zip(s, [set() for _ in range(len(s))]))
for code in codes:
    after[code[1]].add(code[2])
    after[code[0]].add(code[1])
    after[code[0]].add(code[2])
print("".join(sorted(after, key = lambda x: len(after[x]))[::-1]))
