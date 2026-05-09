class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while maxDoubles and target > 1:
                moves += 1 + target % 2
                target >>= 1
                maxDoubles -= 1
        return moves + target - 1