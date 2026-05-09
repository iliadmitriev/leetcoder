class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st: list[str] = []

        for n in num:
            while k and st and st[-1] > n:
                st.pop()
                k -= 1

            if st or n != "0":
                st.append(n)

        st = st[:-k] if k else st

        return "".join(st) or "0"

