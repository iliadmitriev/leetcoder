from bisect import bisect_left


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))

        @cache
        def dfs(i, prev = -1):
            if i == len(arr1):
                return 0

            op = float('inf')

            if arr1[i] > prev:
                op = dfs(i + 1, arr1[i])

            j = bisect_left(arr2, prev + 1)
            if j != len(arr2):
                op = min(op, 1 + dfs(i + 1, arr2[j]))

            return op

        res = dfs(0, -1)
        
        return res if res < float('inf') else -1