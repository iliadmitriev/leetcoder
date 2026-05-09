class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)

        count of subarrays
        k - length of array

        f(1) = 1
        f(2) = 2 + f(1)
        f(3) = 3 + f(2)
        ...
        f(k) = k + f(k - 1)

        S = k * (k + 1) / 2
        """
        total = 0
        curr = 0
        for num in nums:
            if num == 0:
                curr += 1
            else:
                curr = 0
            total += curr
        return total