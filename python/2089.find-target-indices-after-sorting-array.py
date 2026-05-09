class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count_target, count_less = 0, 0
        for num in nums:
            count_target += num == target
            count_less += num < target

        return list(range(count_less, count_less + count_target))