class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        depth = 0
        res = [-1] * n
        
        for i in range(n):
            if seq[i] == '(':
                depth += 1

            res[i] = 1 - depth % 2

            if seq[i] == ')':
                depth -= 1
                
        return res