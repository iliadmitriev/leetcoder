

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()

        # count valid triangles
        # a < b < c and a + b > c
        n = len(nums)

        count = 0

        # for a in range(n):
        #     for b in range(a + 1, n):
        #         c = bisect_left(nums, nums[a] + nums[b], b + 1, n)
        #         count += c - b - 1

        for c in range(n - 1, 1, -1):
            # optimize 1: if c side is so small that all two possble a and b sum will be a triangle
            # then we can count all possible combinations and finish,
            # there will be no greater right bound to check any more (as array is sorted)
            if nums[0] + nums[1] > nums[c]:
                # C(x, 3) = x! / (x - 3)! * 3!
                # C(x, 3) = x * (x - 1) * (x - 2) / 3!
                # x = c + 1 (index to count conversion)
                count += (c + 1) * c * (c - 1) // 6
                break

            # optimize 2: if c is so great than all two possible a and b sum will not be a triangle
            # then we can skip counting all possible combinations
            # and continue to look for smaller c side
            if nums[c - 1] + nums[c - 2] <= nums[c]:
                continue

            a, b = 0, c - 1

            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    # number of indices between a and b (b - a + 1) inclusive
                    # minus one for b side of the triangle (b - a + 1 - 1)
                    count += b - a
                    b -= 1
                else:
                    a += 1

        return count

