class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = (0, 0)
        cache = {cur}

        for move in path:
            match move:
                case 'N': cur = (cur[0], cur[1] + 1)
                case 'S': cur = (cur[0], cur[1] - 1)
                case 'E': cur = (cur[0] + 1, cur[1])
                case 'W': cur = (cur[0] - 1, cur[1])

            if cur in cache:
                return True

            cache.add(cur)

        return False