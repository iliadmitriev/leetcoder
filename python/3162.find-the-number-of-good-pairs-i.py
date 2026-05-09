class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        total = 0

        for i in range(n):
            for j in range(m):
                total += nums1[i] % (nums2[j] * k) == 0

        return total

