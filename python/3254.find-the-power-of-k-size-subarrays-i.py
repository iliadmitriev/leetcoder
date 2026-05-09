class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums

        prev = nums[0] - 1
        res = []
        counter = 1

        for i, cur in enumerate(nums):
            if prev + 1 == cur:
                counter += 1
            else:
                counter = 1

            prev = cur
            if i + 1 < k:
                continue

            if counter >= k:
                res.append(cur)
            else:
                res.append(-1)

        return res

