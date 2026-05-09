class UnionFind:
    def __init__(self, size: int) -> None:
        self.p = list(range(size))
        
    def find(self, x: int) -> int:
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)
        uf = UnionFind(n)
        res = []
        # component index -> list of letters
        letters = defaultdict(list)
        
        for x, y in pairs:
            uf.union(x, y)
            
        for i in range(n):
            letters[uf.find(i)].append(s[i])
            
        for m in letters.values():
            m.sort()
            
        for i in range(n):
            res.append(letters[uf.find(i)].pop(0))
            
        return ''.join(res)