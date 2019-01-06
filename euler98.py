from typing import List, Dict, Tuple

from eulerutil.number_theory import numdigits

words = list([x.replace('"', '') for x in [i.split(",") for i in open('euler98_words.txt')][0]])

def hash_word(word: str) -> int:
    return hash("".join(sorted(word)))

def n_digit_squares(n: int) -> Dict[int, int]:
    sq = {}
    for i in range(int(10**((n-1)*.5)), int(10**(n*.5))+1):
        sq[i] = i**2
    return sq

hashmap = {hash_word(word):[] for word in words}

for word in words:
    hashmap[hash_word(word)].append(word)

for key, value in enumerate(hashmap):
    if len(hashmap[value]) > 1:
        pass
        #print(hashmap[value])
        
anagram_keys = list(filter(lambda x: len(hashmap[x]) > 1, hashmap))
anagrams = sorted([hashmap[key] for key in anagram_keys], key = lambda x: len(x[0]))

def anagram_to_num(word_pair: List[str],
                   sq_list: Dict[int, int],
                   anagram_list: List[List[str]]) -> Dict[int, str]:
    possible_mappings = []
    for v in sq_list.values():
        if len(set(str(v))) == len(set(word_pair[0])):
            #print(v, set(str(v)), set(word_pair[0]))
            possible_mappings.append(dict(zip(word_pair[0], str(v))))
    
    for mapping in possible_mappings:
        output = int("".join([mapping[char] for char in word_pair[1]]))
        if output in sq_list.values() and numdigits(int("".join(mapping.values()))) == numdigits(output):
           print(word_pair[0], "".join(mapping.values()), word_pair[1], output)
    return possible_mappings

squares = n_digit_squares(5)
try:
    for ana in anagrams:
        anagram_to_num(ana, squares, anagrams)
except:
    pass
