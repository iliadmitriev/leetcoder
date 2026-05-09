

class Solution:
    def pivotInteger(self, n: int) -> int:

        prefix, suffix = 0, sum(range(1, n + 1))
        for i in range(1, n + 1):
            prefix += i
            if prefix == suffix:
                return i
            suffix -= i

        return -1

