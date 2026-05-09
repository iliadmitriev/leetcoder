class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 1 << 32
        alpha = '0123456789abcdef'
        ans = ''
        while num:
            num, rem = divmod(num, 16)
            ans = alpha[rem] + ans
        return ans