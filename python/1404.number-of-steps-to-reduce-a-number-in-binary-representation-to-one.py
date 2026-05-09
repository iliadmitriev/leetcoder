class Solution:
    def numSteps(self, s: str) -> int:
        moves = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            digit = ord(s[i]) - ord("0") + carry
            moves += 1 + (digit % 2)

            carry = (digit + 1) // 2

        return moves + carry

