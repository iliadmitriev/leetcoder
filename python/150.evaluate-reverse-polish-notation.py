from math import floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+': (lambda a, b: a + b),
            '-': (lambda a, b: a - b),
            '*': (lambda a, b: a * b),
            '/': (lambda a, b: a / b),
        }

        stack = []
        for token in tokens:
            if token in '+-/*':
                a = stack.pop()
                b = stack.pop()
                res = op[token](b, a)
                stack.append(int(res))
            else:
                stack.append(int(token))

        return stack[-1]
