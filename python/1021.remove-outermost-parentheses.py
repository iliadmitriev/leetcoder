class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = []
        for char in s:
            if char == '(' and depth > 0:
                result.append(char)
            elif char == ')' and depth > 1:
                result.append(char)
            
            depth += 1 if char == '(' else -1
        return ''.join(result)