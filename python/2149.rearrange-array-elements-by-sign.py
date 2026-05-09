class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        n = len(nums)

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        nums[0 : n : 2] = pos
        nums[1 : n : 2] = neg

        return nums