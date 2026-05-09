class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changes = 0
        for i in range(1, len(nums)):
            # compare previous number with current
            if nums[i - 1] > nums[i]:
                changes += 1
                if changes > 1:
                    return False
                # change current number if it's possible
                # check if number befor previous is greater
                # than current
                #       *
                # 3, 5, 4
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                # can't just grow current number uncoditionally
                # because of cases when [4, 2, 3]
                # number befor previous is greater 
                # than both numbers
        return True
                    