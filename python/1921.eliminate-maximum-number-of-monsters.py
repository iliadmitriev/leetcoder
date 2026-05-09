class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        t = lambda x: dist[x] / speed[x]
        data = sorted(range(len(dist)), key=t)
        for i, x in enumerate(data):
            if t(x) <= i:
                return i
        return len(dist)