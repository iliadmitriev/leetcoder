class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        res = 0
        k -= 1

        while k:
            t = k.bit_length() - 1
            k -= 1 << t

            res += operations[t]

        return chr(ord("a") + res % 26)

