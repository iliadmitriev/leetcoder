class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dp(opening: int, closing: int, s: str):
            if opening == 0 and closing == 0:
                res.append(s)

            if opening > closing:
                return

            if opening:
                dp(opening - 1, closing, s + '(')

            if closing:
                dp(opening, closing - 1, s + ')')

        dp(n, n, '')
        return res