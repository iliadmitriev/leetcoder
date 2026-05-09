class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        st = []
        counter = 0

        for ch in s:
            if ch == "(":
                st.append("(")
            elif st and ch == ")":
                st.pop()
            elif ch == ")":
                counter += 1

        return counter + len(st)

