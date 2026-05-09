class Solution:
    def kthCharacter(self, k: int) -> str:
        res = 0
        k -= 1

        while k:
            res += 1
            k &= k - 1

        return chr(ord("a") + res)

