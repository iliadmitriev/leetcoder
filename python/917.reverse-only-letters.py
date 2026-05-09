class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st = list(s)
        i, j = 0, len(st) - 1

        while i < j:
            while i < j and not st[i].isalpha():
                i += 1
            while i < j and not st[j].isalpha():
                j -= 1
            st[i], st[j] = st[j], st[i]
            i += 1
            j -= 1

        return "".join(st)

