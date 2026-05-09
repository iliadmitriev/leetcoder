

class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        p, q = [], []

        for i in range(len(nums)):
            if nums[i] < pivot:
                p.append(nums[i])

            elif nums[i] > pivot:
                q.append(nums[i])

        return p + [pivot] * (len(nums) - len(p) - len(q)) + q

