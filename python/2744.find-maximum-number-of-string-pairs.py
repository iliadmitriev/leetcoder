from collections import defaultdict


class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        count = 0
        mp: dict[str, int] = defaultdict(int)

        for word in words:
            count += mp[word[::-1]]
            mp[word] = 1

        return count

