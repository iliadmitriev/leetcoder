import bisect


class Solution:
    @staticmethod
    def count(nums1, nums2, target):
        total = 0
        for num1 in nums1:
            if num1 > 0:
                t = target // num1
                total += bisect.bisect_right(nums2, t)

            elif num1 < 0:
                t = target // num1 + (1 if target % num1 else 0)
                total += len(nums2) - bisect.bisect_left(nums2, t)

            else:
                if target >= 0:
                    total += len(nums2)

        return total

    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = nums1[0] * nums2[0], nums1[0] * nums2[0]
        for i in [0, len(nums1) - 1]:
            for j in [0, len(nums2) - 1]:
                left = min(left, nums1[i] * nums2[j])
                right = max(right, nums1[i] * nums2[j])

        while left < right:
            mid = (right + left) // 2
            count = self.count(nums1, nums2, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

