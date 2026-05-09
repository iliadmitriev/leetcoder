from itertools import product


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        m, n = len(board), len(board[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def deck(y0, x0):
            for dy, dx in dirs:
                y, x = y0 + dy, x0 + dx
                if 0 <= y < m and 0 <= x < n and board[y][x] == "X":
                    yield y, x

        seen = set()
        ships = 0
        for y0, x0 in product(range(m), range(n)):
            if board[y0][x0] == "X" and (y0, x0) not in seen:
                stack = [(y0, x0)]
                seen.add((y0, x0))
                while stack:
                    y, x = stack.pop()
                    for yn, xn in deck(y, x):
                        if (yn, xn) not in seen:
                            stack.append((yn, xn))
                            seen.add((yn, xn))
                ships += 1
        return ships