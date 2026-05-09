class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = reduce(lambda d, x: 10 * d + x, num, 0)
        res = list(map(int, str(k + n)))
        return res