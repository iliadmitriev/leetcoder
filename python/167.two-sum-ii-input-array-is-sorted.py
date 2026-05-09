class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in cache:
                return [cache[diff], i + 1]
            else:
                cache[num] = i + 1
