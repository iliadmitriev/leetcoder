class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n

        if k == 0:
            return res

        left, right = 1, k + 1
        if k < 0:
            left, right = n + k, n

        window = sum(code[left:right])

        for i in range(n):
            res[i] = window
            window += code[(i + right) % n] - code[(i + left) % n]

        return res

