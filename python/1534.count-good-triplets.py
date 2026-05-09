import bisect


class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        """
        NOTE:
            abs(i - j) <= a, means
            i: [j - a, j + a]

            abs(j - k) <= b, means
            k: [j - b, j + b]
        """

        count = 0
        n = len(arr)

        for j in range(n - 2, -1, -1):
            # collect ordered list of elements between j and n
            # that fits [arr[j] - b, arr[j] + b]
            arr_b = []
            for k in range(j + 1, n):
                diff = arr[j] - arr[k]
                if abs(diff) <= b:
                    bisect.insort_right(arr_b, diff)

            for i in range(0, j):
                diff = arr[i] - arr[j]
                if abs(diff) <= a:
                    lower = bisect.bisect_left(arr_b, -c - diff)
                    upper = bisect.bisect_right(arr_b, c - diff)

                    count += upper - lower

        return count

