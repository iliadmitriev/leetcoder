class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i, j = 0, 0
        l, r = 0, 0
        cur = 0

        while i < len(num):
            j = i + 1
            while j < len(num) and num[i] == num[j] and j - i < 3:
                j += 1

            if j - i == 3 and cur <= 3 * (ord(num[i]) - 48):
                l, r = i, j
                cur = 3 * (ord(num[i]) - 48)

            i = j

        return num[l: r]