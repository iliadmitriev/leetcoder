class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        n -> row (start from 1)
        k -> index

        1 - 0
        2 - 01
        3 - 0110
        4 - 01101001
        5 - 0110100110010110
        6 - 01101001100101101001011001101001

        Binary Search Tree approach

          0        1
        0   1    1   1

        """
        cur = 0
        left, right = 1, 2 ** (n - 1)

        for _ in range(n - 1):
            mid = (left + right) // 2

            if k > mid:
                left = mid + 1
                cur = 1 - cur
            else:
                right = mid

        return cur