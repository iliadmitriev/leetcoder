class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        win = [0, 0, 0]
        left = 0
        n = len(s)

        for right in range(n):
            win[ord(s[right]) - ord("a")] += 1

            while win[0] and win[1] and win[2]:
                win[ord(s[left]) - ord("a")] -= 1
                left += 1

            count += left

        return count

