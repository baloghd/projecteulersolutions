from itertools import permutations

class ngonRing:
    def __init__(self, n):
        self.n = n
        self.extnodes = {i: 0 for i in range(1, n + 1)}
        self.ring =     {i: 0 for i in range(1, n + 1)}
        self.p = permutations(range(1, 2*n + 1))
        self.unique_str = ""
        self.seen_triplets = set()
        
    def fill(self) -> None:
        l = list(next(self.p))
        if len(set(filter(lambda x: x > 5, l[self.n:]))) > 0:
            return False
        self.extnodes = dict(zip(self.extnodes, l))
        self.ring = dict(zip(self.ring, l[self.n:]))
        return True
        
    def rules_pass(self) -> bool:
        equations = self.extnodes[1] + self.ring[1] + self.ring[2]
        for x in range(1, self.n + 1):
            ne = 1 if x == self.n else x + 1
            t = self.extnodes[x] + self.ring[x] + self.ring[ne]
            if t != equations:
                return False
        return True
    
    def describe(self) -> None:
        self.unique_str = ""
        for x in range(1, self.n + 1):
            ne = 1 if x == self.n else x + 1
            triplet = "".join(map(str, [self.extnodes[x], self.ring[x], self.ring[ne]]))
            if triplet in self.seen_triplets:
                self.unique_str += "s"
                break
            else:
                self.unique_str += triplet
                self.seen_triplets.add(triplet)

if __name__ == '__main__':
    r = ngonRing(5)
    while True:
        if r.fill() and r.rules_pass():
            r.describe()
            if len(r.unique_str) == 16:
                    print(r.extnodes, r.ring, r.unique_str)
   
