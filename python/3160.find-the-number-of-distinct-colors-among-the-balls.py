class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        colors = {}
        balls = {}
        res = []

        for ball, color in queries:
            prev = balls.get(ball, 0)
            balls[ball] = color

            colors[color] = colors.get(color, 0) + 1

            if prev > 0:
                colors[prev] -= 1

                if colors[prev] == 0:
                    del colors[prev]

            res.append(len(colors))

        return res

