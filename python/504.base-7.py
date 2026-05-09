class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        sign = num < 0
        if sign:
            num = -num

        res = []
        while num:
            num, r = divmod(num, 7)
            res.append(str(r))

        if sign:
            res.append("-")

        return "".join(res[::-1])

