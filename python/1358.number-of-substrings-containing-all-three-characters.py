class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        a = ord("a")
        win = [0,0,0]
        res = 0

        l = 0
        for r in range(n):
            win[ord(s[r]) - a] += 1

            while win[0] and win[1] and win[2]:
                res += n - r # add the rest of string l times

                win[ord(s[l]) - a] -= 1
                l += 1

        return res
        