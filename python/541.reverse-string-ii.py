class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        st = list(s)
        n = len(st)

        for i in range(0, n, 2 * k):
            st[i: i + k] = st[i: i + k][::-1]

        return "".join(st)

