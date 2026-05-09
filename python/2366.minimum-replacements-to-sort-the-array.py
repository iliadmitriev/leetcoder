class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        # answer 
        replacements = 0

        # start from one but last element (last one is always sorted)
        for i in range(n - 2, -1, -1):
            # skip if nothing to do (already sorted in non descending order)
            if nums[i] <= nums[i + 1]:
                continue

            # count how many elements you get after replacement
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]

            # add number of operations (count - 1) to answer
            replacements += num_elements - 1

            # get the leftmost value after replacement 
            nums[i] //= num_elements

        return replacements