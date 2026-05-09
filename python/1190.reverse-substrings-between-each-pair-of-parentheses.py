class Solution:
    def reverseParentheses(self, s: str) -> str:
        res: list[str] = []
        stack: list[int] = []

        for c in s:
            if c == "(":
                stack.append(len(res))
            elif c == ")":
                ind = stack.pop()
                res[ind:] = res[ind:][::-1]
            else:
                res.append(c)

        return "".join(res)

