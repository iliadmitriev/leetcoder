class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10:
            tmp = 0
            while num:
                num, rem = divmod(num, 10)
                tmp += rem
            num = tmp
        return num