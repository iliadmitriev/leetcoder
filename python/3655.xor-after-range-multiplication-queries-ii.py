import collections as col
import math
import functools
import operator


class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = int(1e9) + 7
        n = len(nums)
        limit = math.isqrt(n)
        # a mapping of dense queries grouped by step size
        # k -> list of [l, r, v]
        dense = col.defaultdict(list[list[int]])

        def inv_mod(x: int) -> int:
            """Inverse x -> 1/x by modulo MOD.

            if p is prime:             x^(p - 1) = 1 (mod p)
            divide both sides by x:    x^(p - 2) = x^(-1) (mod p)
            """
            return pow(x, MOD - 2, MOD)

        # iterate all queries: range left, right, step, value
        for l, r, k, v in queries:
            if k >= limit:  # if step is sparse
                for i in range(l, r + 1, k):  # then apply it to array right now
                    nums[i] *= v
                    nums[i] %= MOD

            else:  # otherwise save it for later
                dense[k].append((l, r, v))

        # apply dense queries group-wise
        for k, q in dense.items():
            mul = [1] * n  # list of multipliers, i.e [1,1,1,1,1,1,1,1,1,1]

            # iterate group of queries
            for l, r, v in q:
                # set left and right multipliers,i.e l=2, r=6, v=3 [1,1,3,1,1,1,3^(-1),1,1,1]
                mul[l] *= v
                mul[l] %= MOD

                # and the right one (if it is within a bounds)
                steps = (r - l) // k
                next_step = l + (steps + 1) * k

                if next_step < n:
                    mul[next_step] *= inv_mod(v)
                    mul[next_step] %= MOD

            # apply whole group of multipliers
            for i in range(n):
                if i >= k:
                    mul[i] *= mul[i - k]
                    mul[i] %= MOD

                nums[i] *= mul[i]
                nums[i] %= MOD

        return functools.reduce(operator.xor, nums)
