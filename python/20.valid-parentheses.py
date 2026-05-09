class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        open_brackets = set(brackets.values())
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
        return not stack