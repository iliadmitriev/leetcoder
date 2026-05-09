class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        if n == 1:
            return "0"

        k -= 1
        inv = 0  # inverstions count
        mid = pow(2, n - 1) - 1

        while k > 0:
            if k > mid:
                k = 2 * mid - k
                inv += 1

            mid //= 2

        if inv & 1:
            return "1"

        return "0"
