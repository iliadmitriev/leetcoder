from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Time: O(N + K**2)
        Space: O(K)
        """
        freq = Counter(s)
        deletions = 0
        found = set()

        for fr in sorted(freq.values(), reverse=True):

            while fr and fr in found:
                fr -= 1
                deletions += 1

            found.add(fr)
        
        return deletions