class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        sumA, sumB = sum(nums1), sum(nums2)
        zeroA, zeroB = nums1.count(0), nums2.count(0)

        if zeroA == 0 and zeroB + sumB > sumA:
            return -1

        if zeroB == 0 and zeroA + sumA > sumB:
            return -1

        return max(sumA + zeroA, sumB + zeroB)

