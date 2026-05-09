class Solution:
    def maxOperations(self, s: str) -> int:
        inc = 0
        cnt = 0
        prev = ""

        for i in range(len(s) - 1, -1, -1):
            if prev != "0" and s[i] == "0":
                inc += 1

            elif s[i] == "1":
                cnt += inc

            prev = s[i]

        return cnt

