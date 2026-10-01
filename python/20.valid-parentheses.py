class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []

        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif not stack or ch != brackets[stack[-1]]:
                return False
            else:
                stack.pop()

        return not stack