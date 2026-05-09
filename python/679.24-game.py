import math


class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        EPS = 1e-7

        def dfs(cards: list[int | float]) -> bool:
            if len(cards) == 1:
                return math.isclose(cards[0], 24, rel_tol=EPS)

            for i in range(len(cards)):
                for j in range(i + 1, len(cards)):
                    a, b = cards[i], cards[j]
                    new_cards = cards[:i] + cards[i + 1 : j] + cards[j + 1 :]
                    ops = [a + b, a - b, b - a, a * b]
                    if b > EPS:
                        ops.append(a / b)
                    if a > EPS:
                        ops.append(b / a)

                    for op in ops:
                        new_cards.append(op)
                        if dfs(new_cards):
                            return True
                        new_cards.pop()

            return False

        return dfs(list(map(float, cards)))

