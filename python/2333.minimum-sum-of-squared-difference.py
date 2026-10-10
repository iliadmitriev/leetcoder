class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        n = len(nums1)
        ops = k1 + k2
        mx = 0
        
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            nums1[i] = diff
            mx = max(mx, diff)

        diff_count = [0] * (mx + 1)
        for diff in nums1:
            diff_count[diff] += 1

        for diff in range(mx, 0, -1):
            op = min(ops, diff_count[diff])

            diff_count[diff] -= op
            ops -= op
            diff_count[diff - 1] += op

            if ops == 0:
                break

        res = 0
        for diff in range(1, mx + 1):
            res += diff * diff * diff_count[diff]

        return res
