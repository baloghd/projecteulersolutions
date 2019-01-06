from typing import Set

def get_term_set(a: int, b: int) -> Set[int]:
    s = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            if i**j not in s:
                s.add(i**j)
    return s

print(len(get_term_set(100, 100)))
