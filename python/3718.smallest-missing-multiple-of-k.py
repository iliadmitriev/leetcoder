class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        s = {n // k - 1 for n in nums if n % k == 0}

        for c in itertools.count():
            if c not in s:
                return (c + 1) * k

        return k