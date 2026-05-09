class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        k = max(m, n)
        res = []

        carry = 0

        for i in range(k):
            x = int(num1[m - i - 1]) if i < m else 0
            y = int(num2[n - i - 1]) if i < n else 0

            res.append(str((x + y + carry) % 10))
            carry = (x + y + carry) // 10

        if carry:
            res.append(str(carry))

        return "".join(res[::-1])

