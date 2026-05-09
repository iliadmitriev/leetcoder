class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l = r = k
        max_score = nums[k]
        curr = nums[k]

        while l > 0 or r < len(nums) - 1:
            left = nums[l - 1] if l > 0 else 0
            right = nums[r + 1] if r < len(nums) - 1 else 0

            if left > right:
                l -= 1
                curr = min(curr, left)
            else:
                r += 1
                curr = min(curr, right)

            max_score = max(max_score, curr * (r - l + 1))

        return max_score
        