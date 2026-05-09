class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:

        i = 0
        n = len(bits)

        while i < n:
            if i == n - 1:
                return True

            if bits[i] == 0:
                i += 1
            else:
                i += 2

        return False

