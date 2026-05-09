class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        Func https://oeis.org/A005563
        a(n) = n*(n+2) = (n+1)^2 - 1.
        row 0, 3, 8, 15, 24, 35, 48, 63, 80, 99, 120, 143, 168, 195 ...
        is a bit position of powered on bulbs
        """
        # if n == 0:
        #     return 0
        # get_bin = lambda x, n: format(x, 'b').zfill(n)

        # bulbs = (1 << (n)) - 1
        # print(get_bin(bulbs, n))
        # for i in range(2, n + 1):
        #     for j in range(i - 1, n, i):
        #         bulbs = bulbs ^ (1 << j)
        #     print(get_bin(bulbs, n))
        func = lambda x: x * (x + 2)

        # i = 0
        # j = func(i)
        # while j < n:
        #     i += 1
        #     j = func(i)

        # print(d)
        # print(bulbs, get_bin(bulbs, n))
        
        # return i
        # return int(sqrt(n))

        lo, hi = 0, n

        while lo < hi:
            mid = (lo + hi) // 2

            if func(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
