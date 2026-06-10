import heapq


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """
        Implementation with sparse table algorithm
        Key: requiremts for this approach (idempotency)

        Problem:
        calculate idempotent function `fn` (`max`, `min` ...) over a range of immutable array `arr[i]` with length N

        Idempotency:

        f(f(x)) = f(x), single operand
        f(f(x, y), y) = f(x, y), two operands

        Examples: max, min, gcd, and, or

        max(b, max(a, max(a, b))) == max(a, b)
        or(b, or(a, or(a, b))) == or(a, b)

        Counter examples: sum

        sum(a, b) != sum(a, sum(a, b))

        Each range can be covered with one (corner case if length K = 2^n, n - natural) or two intervals (can overlap).
        We don't care about overlapping (function is idempotent):

        [L, R], K = R - L + 1 (length)

        two intervals: [L : L + 2^n] + [R - 2^n : R]

        st[i][j] - i - start index, 2^j length (j = 0, 1, 2, 3... => 1, 2, 4, 8, ...)

        Build (arr, N):
        base case: j = 0: st[i][0] = arr[i]
        recursive: j > 0: st[i][j] = fn(st[i][j-1], st[i + 2^(j - 1)][j - 1])
        up to: 0 .. [log_2(N)]

        Query (L, R):
        1. length: K = R - L + 1
        2. j = log_2(K)
        3. res = fn(st[L][j], st[R - 2^j + 1][j])
          - L block: st[L][j]
          - R block: st[R - 2^j + 1][j]

        Note: can cache [log_2(x)], x = 0..N
        """
        n = len(nums)
        logn = n.bit_length()

        st_max = [[0] * logn for _ in range(n)]
        st_min = [[0] * logn for _ in range(n)]

        # set base case st[i][0] = arr[i]
        for i in range(n):
            st_max[i][0] = st_min[i][0] = nums[i]

        # calculate up to log_2(N)
        for j in range(1, logn):
            step = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + step][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + step][j - 1])

        def query_max(l: int, r: int) -> int:
            k = r - l + 1
            j = k.bit_length() - 1
            return max(st_max[l][j], st_max[r - (1 << j) + 1][j])

        def query_min(l: int, r: int) -> int:
            k = r - l + 1
            j = k.bit_length() - 1
            return min(st_min[l][j], st_min[r - (1 << j) + 1][j])

        # all negative to make a max heap
        pq = [
            (-(query_max(l, n - 1) - query_min(l, n - 1)), l, n - 1) for l in range(n)
        ]

        heapq.heapify(pq)

        ans = 0

        for _ in range(k):
            v, l, r = heapq.heappop(pq)
            ans -= v  # convert back from stored negative to original positive before adding to result

            if r > l:
                heapq.heappush(
                    pq, (-(query_max(l, r - 1) - query_min(l, r - 1)), l, r - 1)
                )

        return ans
