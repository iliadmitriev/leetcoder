

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        def scs(i: int, j: int) -> str:
            """TLE / MLE."""
            if i == len(str1):
                return str2
            if j == len(str2):
                return str1

            if str1[0] == str2[0]:
                return str1[0] + scs(i + 1, j + 1)

            a = str1[i] + scs(i + 1, j)
            b = str2[j] + scs(i, j + 1)

            if len(a) < len(b):
                return a
            return b

        N, M = len(str1), len(str2)
        prev = [str2[j:] for j in range(M)]
        prev.append("")

        for i in reversed(range(N)):
            cur = [""] * M
            cur.append(str1[i:])

            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j + 1]
                else:
                    a = str1[i] + prev[j]
                    b = str2[j] + cur[j + 1]
                    if len(a) < len(b):
                        cur[j] = a
                    else:
                        cur[j] = b

            prev = cur

        return prev[0]

