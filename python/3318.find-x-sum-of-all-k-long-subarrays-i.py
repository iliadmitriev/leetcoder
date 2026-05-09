import collections


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        def topX(arr: dict[int, int], x: int) -> int:
            top = sorted(arr.items(), key=lambda x: (x[1], x[0]), reverse=True)
            top = top[:x]
            return sum(k * v for k, v in top)

        window = collections.defaultdict(int)
        ans = []
        n = len(nums)

        for i in range(0, k):
            window[nums[i]] += 1

        ans.append(topX(window, x))

        for i in range(k, n):
            window[nums[i - k]] -= 1
            window[nums[i]] += 1
            ans.append(topX(window, x))

        return ans

