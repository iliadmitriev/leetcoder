class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        A, B, C = True, False, nums[0] == nums[1]

        for i in range(2, n):
            A, B, C = B, C, (
                B and nums[i] == nums[i - 1]  # 2 are equal
                or A and (
                    nums[i - 2] == nums[i - 1] == nums[i]  # 3 are equal
                    or nums[i - 2] + 2 == nums[i - 1] + 1 == nums[i]  # 3 are consecutive
                    )
            )

        return C