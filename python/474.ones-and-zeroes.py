class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        data = list(map(lambda s: (s.count("0"), s.count("1")), strs))
        
        @cache
        def dfs(i: int, j: int, idx: int) -> int:
            if i < 0 or j < 0:
                return -math.inf
            
            if idx == len(strs):
                return 0
            
            return max(dfs(i, j, idx + 1), 1 + dfs(i - data[idx][0], j - data[idx][1], idx + 1))
        
        return dfs(m, n, 0)