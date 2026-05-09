class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """Find k-th smallest number in multiplication table
        Binary search approach

        :param m: number of rows
        :param n: number of columns
        :param k: smallest k-th should be returned
        :return: k-th smallest number
        """

        def count_values_less_than(x):
            # count - is how many values in the table
            # is less or equal to x
            # it's calculated as sum of (x // i)
            # amount of values in a row
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        # lo is 1, and highest is m * n
        lo, hi = 1, m * n
        # while lower and higher bounds don't match
        while lo < hi:
            # calculate middle value
            mi = (lo + hi) // 2
            # count how many values is there is our table
            # that is lower than middle
            count = count_values_less_than(mi)
            # if we exceeded our k than move hi bound to middle
            if count >= k:
                hi = mi
            else:
                lo = mi + 1
        return lo
