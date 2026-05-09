class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        cnt2 = num2.bit_count()
        N = max(num1, num2).bit_length()

        x = 0
        for i in range(N - 1, -1, -1):
            if cnt2 == 0:
                break

            if (num1 >> i) & 1:
                x |= 1 << i
                cnt2 -= 1

        for i in range(N):
            if cnt2 == 0:
                break

            if (num1 >> i) & 1 == 0:
                x |= 1 << i
                cnt2 -= 1

        return x

