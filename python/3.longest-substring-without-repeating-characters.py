class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        j = 0
        visited = [False] * 256

        for i in range(n):

            while visited[ord(s[i])]:
                visited[ord(s[j])] = False
                j += 1

            visited[ord(s[i])] = True
            
            res = max(res, i - j + 1)

        return res
