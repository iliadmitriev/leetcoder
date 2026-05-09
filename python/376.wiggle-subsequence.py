class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        n = len(nums)
        # make first step
        up, down = 1, 1

        for i in range(1, n):
            # save previous numbers
            up_prev, down_prev = up, down

            # if current number is larger then previous
            if nums[i] > nums[i - 1]:
                # wiggle from down to up
                up = down_prev + 1
                down = down_prev
            
            # if current numeber is less than previous
            elif nums[i] < nums[i - 1]:
                # wiggle from down to up
                up = up_prev
                down = up_prev + 1
            
            # if numbers are equal
            else:
                # don't wiggle
                up = up_prev
                down = down_prev

        # return max of numbers
        return max(up, down)