class Solution:

    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        _base = 26
        _bias = ord("a")
        st = [0] * n
        prefix = [0] * (n + 1)

        for i in range(n):
            st[i] = ord(s[i]) - _bias

        for start, end, _dir in shifts:
            _dir = 2 * _dir - 1
            prefix[start] += _dir
            prefix[end + 1] -= _dir

        cur = 0
        for i in range(n):
            cur += prefix[i]
            st[i] = (st[i] + cur) % _base

        return "".join(chr(v + _bias) for v in st)


