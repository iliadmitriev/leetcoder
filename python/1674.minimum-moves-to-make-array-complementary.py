# @leet start
class Solution:
    def minMoves(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        diff[2] += n  # worst case need to change all the numbers a + b < 2

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]

            if a > b:
                a, b = b, a

            diff[a + 1] -= 1  # one of numbers can be left untouched, other changed
            diff[a + b] -= 1  # both numbers can be left untouched
            diff[a + b + 1] += 1  # one of numbers have to be changed
            diff[b + limit + 1] += 1  # both numbers have to be changed

        min_moves = n
        moves = 0

        for target in range(2, 2 * limit + 1):
            moves += diff[target]
            min_moves = min(min_moves, moves)

        return min_moves


# @leet end
