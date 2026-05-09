class Solution:
    def numTrees(self, n: int) -> int:
        """Catalan numbers

        O(n)
        O(1)
        """
        return int(reduce(operator.mul, ((4 * i + 2) / (i + 2) for i in range(n)), 1))
