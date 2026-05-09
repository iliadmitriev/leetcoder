class Solution:
    def largestOddNumber(self, num: str) -> str:
        j = 0
        for i in range(len(num) -1, -1, -1):
            if ord(num[i]) % 2:
                j = i + 1
                break

        return num[:j]