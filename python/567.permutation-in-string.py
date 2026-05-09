class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m = len(s1)

        if m > len(s2):
            return False

        pattern = [0] * 26

        for ch in s1:
            pattern[ord(ch) - 97] += 1

        window = [0] * 26

        for i in range(len(s2)):
            window[ord(s2[i]) - 97] += 1

            if i >= m:
                window[ord(s2[i - m]) - 97] -= 1

            if i >= m - 1:
                if window == pattern:
                    return True

        return False

