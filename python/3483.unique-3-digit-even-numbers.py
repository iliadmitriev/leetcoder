class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cur = 0
        vis = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                
                for k in range(n):
                    if k == i or k == j:
                        continue

                    cur = 100 * digits[i] + 10 * digits[j] + digits[k]

                    if cur >= 100 and cur % 2 == 0:
                        vis.add(cur)

        return len(vis)
        