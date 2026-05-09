"""
         +
     *
[0,1,2,2,3,0,4,2]   val = 2
+i = 0
*j = 0

не равно: инкр оба
равно: инкр i
пишем из i в j

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[j] = nums[i]
                j += 1
        return j