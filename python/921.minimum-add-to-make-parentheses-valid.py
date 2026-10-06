class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        st = 0
        counter = 0

        for ch in s:
            if ch == "(":
                st += 1
            elif st and ch == ")":
                st -= 1
            elif ch == ")":
                counter += 1

        return counter + st

