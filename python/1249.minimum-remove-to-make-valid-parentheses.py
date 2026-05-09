class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        stack = []

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

            res.append(ch)

        while stack:
            res.pop(stack.pop())

        return "".join(res)

