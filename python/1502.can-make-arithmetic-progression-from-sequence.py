class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        it = iter(sorted(arr))
        a, b = next(it), next(it)
        prev, step = b, b - a

        for curr in it:
            if step != curr - prev:
                return False
            prev = curr
        return True
