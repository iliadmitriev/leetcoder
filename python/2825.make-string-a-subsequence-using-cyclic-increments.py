

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        if m < n:
            return False

        i, j = 0, 0
        while i < m and j < n and m - i >= n - j:
            if ord(str2[j]) - 97 in (ord(str1[i]) - 97, (ord(str1[i]) - 96) % 26):
                j += 1

            i += 1

        if j == n:
            return True

        return False


