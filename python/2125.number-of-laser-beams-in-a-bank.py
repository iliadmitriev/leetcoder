class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for row in bank:
            n = row.count('1')
            if n:
                res += prev * n
                prev = n
        return res