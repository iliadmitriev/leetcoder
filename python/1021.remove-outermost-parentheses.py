class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        d = 0
        for ch in s:
            if ch =="(" and d > 0:
                res.append(ch)
            elif ch == ")" and d > 1:
                res.append(ch)
            
            if ch == "(":
                d += 1
            elif ch == ")":
                d -= 1
                
        return "".join(res)
                
        