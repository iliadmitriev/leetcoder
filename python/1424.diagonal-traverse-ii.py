class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        queue = deque([(0, 0)])

        while queue:
            row, col = queue.popleft()
            res.append(nums[row][col])

            # add lower cell for the first cell in column
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))

            # add left cell for all cells 
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return res