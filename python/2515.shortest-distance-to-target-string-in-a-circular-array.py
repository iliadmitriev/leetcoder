class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = n

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                min_dist = min(min_dist, dist, n - dist)

        if min_dist == n:
            return -1
        return min_dist
        