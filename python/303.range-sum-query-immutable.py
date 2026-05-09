from itertools import accumulate
import operator

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.acc = [0] * (n + 1)
        for i in range(1, n + 1):
            self.acc[i] = nums[i - 1] + self.acc[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right + 1] - self.acc[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)