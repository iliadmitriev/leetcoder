class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digits(x: int) -> int:
            y = 0
            while x:
                x, r = divmod(x, 10)
                y += r
            return y

        for i, x in enumerate(nums):
            if i == digits(x):
                return i
        
        return -1
        