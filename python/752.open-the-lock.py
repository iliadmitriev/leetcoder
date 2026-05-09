from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        q: deque[tuple[str, int]] = deque()
        visited: set[str] = set(deadends)

        q.append(("0000", 0))

        if target in visited or "0000" in visited:
            return -1

        visited.add("0000")

        while q:
            code, dist = q.popleft()

            if code == target:
                return dist

            for i in range(4):
                for d in (-1, 1):
                    new_code = code[:i] + str((int(code[i]) + d) % 10) + code[i + 1 :]
                    if new_code not in visited:
                        visited.add(new_code)
                        q.append((new_code, dist + 1))
        return -1

