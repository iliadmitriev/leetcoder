class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []  # stack of chars

        for c in s:

            st.append(c)

            if len(st) >= len(part):

                i = 0
                j = len(st) - len(part)

                while i < len(part) and j < len(st) and st[j] == part[i]:
                    i += 1
                    j += 1

                if i == len(part):
                    st = st[: -len(part)]

        return "".join(st)

