class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Permutations:
        
        P_n = A^n_n = n! / (n - n)! = n!

        """
        def rev(x: int) -> None:
            """
            function to reverse elements from x to last element
            """
            nums[x:len(nums)] = reversed(nums[x:len(nums)])
        
        def swap(i: int, j: int) -> None:
            """
            function to swap i-th and j-th element of nums
            """
            nums[i], nums[j] = nums[j], nums[i]
            
        # starting from last but one element
        i = len(nums) - 2
        # find i-th element which is strictly smaller than (i+1)-th right
        while i >= 0 and nums[i + 1] <= nums[i]:
            # move left
            i -= 1
        
        # if we found that element i != -1
        if i >= 0:
            # start from the last element
            j = len(nums) - 1
            # find first element which is bigger than i-th
            while nums[j] <= nums[i]:
                j -= 1
                        
            swap(i, j)
        
        rev(i + 1)