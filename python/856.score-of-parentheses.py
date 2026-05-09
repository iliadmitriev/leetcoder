class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        
        stack = []
        # current result
        curr = 0
        
        for ch in s:
            if ch == '(':
                stack.append(curr)
                curr = 0
            elif ch == ')':       
                curr += stack.pop() + max(curr, 1)
        
        return curr