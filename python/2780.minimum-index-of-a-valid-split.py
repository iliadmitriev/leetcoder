

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        def getDominant(arr: list[int]) -> int:
            res, cnt = -1, 0
            for num in arr:
                if cnt == 0:
                    res = num
                if num == res:
                    cnt += 1
                else:
                    cnt -= 1

            return res

        n = len(nums)
        dom = getDominant(nums)
        cnt = nums.count(dom)

        if dom == -1 or cnt * 2 <= n:
            return -1

        left, right = 0, cnt
        for i in range(len(nums)):
            if nums[i] == dom:
                left += 1
                right -= 1

            if left * 2 > (i + 1) and 2 * right > (n - i - 1):
                return i

        return -1

