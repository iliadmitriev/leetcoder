

class Solution:
    @staticmethod
    def bin_search(arr: list[int], target: int) -> int:
        lo, hi = 0, len(arr) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False

    def longestSquareStreak(self, nums: list[int]) -> int:
        nums.sort()

        longestStreak = -1
        limit = 10**5
        cache = set()

        for num in nums:

            if num in cache:
                continue

            cache.add(num)

            cur = 1
            curNum = num

            while curNum * curNum <= limit:
                if not self.bin_search(nums, curNum * curNum):
                    break

                curNum *= curNum
                cur += 1

            longestStreak = max(longestStreak, cur)

        if longestStreak < 2:
            return -1

        return longestStreak

