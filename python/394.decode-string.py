class Solution:
    def decodeString(self, s: str) -> str:
        """
     
        Example:
            
            3[a]2[bc]
            aaabcbc
                
        """
        stack = deque()
        # res - alpha accumulator
        # n - digit accumulator
        res, n = str(), str()
        
        for char in s:
            
            if char.isalpha():
                res += char
                
            elif char.isdigit():
                n += char
            
            # if we met open bracket save to stack current state
            # and reset state
            elif char == '[':
                stack.append((n, res))
                res, n = str(), str()
        
            # if we met close bracket
            # get count and previously saved string from stack
            # add to previous string current accumulated res multiplied by count
            elif char == ']':
                cnt, prev = stack.pop()
                res = prev + res * int(cnt)
        
        return res