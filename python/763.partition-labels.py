

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i

        j = 0
        end = 0
        ans = []
        for i, c in enumerate(s):
            end = max(end, last[ord(c) - ord('a')])

            if i == end:
                ans.append(i - j + 1)
                j = i + 1

        return ans
        