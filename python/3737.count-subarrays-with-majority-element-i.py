# class Solution:
#     def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
#         cnt = 0
#         res = 0

#         for l in range(len(nums)):

#             # Boyer-Moore majority voating
#             cnt = 0

#             for r in range(l, len(nums)):
#                 if nums[r] == target:
#                     cnt += 1
#                 else:
#                     cnt -= 1

#                 if cnt > 0:
#                     res += 1

#         return res


class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        res = 0

        cnt = defaultdict(int)
        acc = defaultdict(int)

        pre = n + 1
        cnt[pre] = 1
        acc[pre] = 1

        for num in nums:
            if target == num:
                pre += 1
            else:
                pre -= 1

            cnt[pre] += 1
            acc[pre] = acc[pre - 1] + cnt[pre]

            res += acc[pre - 1]

        return res
