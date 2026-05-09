from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # optimize 1: if number of letters in word is less
        # than number of letters in board
        if len(word) > m * n:
            return False

        # optimize 2: if any letter in word is not in board
        board_count = Counter(chain(*board))
        word_count = Counter(word)
        if not any(word_count[c] <= board_count[c] for c in set(word)):
            return False

        # optimize 3: if first letter is more frequest
        # in the board than last letter
        if board_count[word[0]] < board_count[word[-1]]:
            word = word[::-1]

        # use DFS to find is there is a word in the board
        def dfs(r: int, c: int) -> bool:
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
            seen = set()
            stack: list[tuple[int, int, int, bool]] = [(r, c, 0, False)]

            while stack:
                y, x, i, p = stack.pop()

                if p:
                    seen.remove((y, x))
                else:

                    if i >= len(word):
                        continue

                    if word[i] != board[y][x]:
                        continue

                    if i == len(word) - 1:
                        return True

                    seen.add((y, x))
                    stack.append((y, x, i, True))

                    for dy, dx in dirs:
                        ny, nx = y + dy, x + dx
                        if not (0 <= ny < m and 0 <= nx < n):
                            continue
                        if (ny, nx) not in seen:
                            stack.append((ny, nx, i + 1, False))

            return False

        for y in range(m):
            for x in range(n):
                if word[0] == board[y][x] and dfs(y, x):
                    return True
        return False

