from typing import Set
import math

words = list(open("euler42_words.txt"))[0].replace('"', '').split(",")
triangle_limit = math.floor(math.sqrt(max(map(len, words)) * 26 * 2))

def wordplace(c: str) -> int:
    return ord(c) - 65 + 1

def word_to_triangle(w: str) -> int:
    return sum(map(wordplace, w))

def firstntriangles(n: int) -> Set[int]:
    return {n * (n + 1) / 2 for n in range(1, n + 1)}

t = firstntriangles(triangle_limit)

print(sum(1 if word in t else 0 for word in map(word_to_triangle, words)))
