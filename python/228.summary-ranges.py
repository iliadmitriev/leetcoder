class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        j = 0

        for i in range(n):
            if i == n - 1 or nums[i] + 1 != nums[i + 1]:
                if j == i:
                    res.append(f'{nums[i]}')
                else:
                    res.append(f'{nums[j]}->{nums[i]}')
                j = i + 1

        return res


