from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        bannedSet = set(map(str.lower, banned))

        i, j = 0, 0
        n = len(paragraph)

        counter: defaultdict[str, int] = defaultdict(int)

        while i < n:
            while i < n and not paragraph[i].isalpha():
                i += 1

            j = i
            while j < n and paragraph[j].isalpha():
                j += 1

            if j - i > 0 and paragraph[i:j].lower() not in bannedSet:
                counter[paragraph[i:j].lower()] += 1

            i = j

        return max(counter.keys(), key=counter.get)

