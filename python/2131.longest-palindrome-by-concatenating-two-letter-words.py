class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        total = 0

        cache = {}
        for word in words:
            if word not in cache:
                cache[word] = 0

            cache[word] += 1

        center = False
        for word, count in cache.items():
            if word[0] == word[1]:
                total += count // 2 * 4
                if count % 2 == 1:
                    center = True
            elif word[::-1] not in cache:
                continue
            else:
                total += min(cache[word[::-1]], count) * 2

        if center:
            total += 2

        return total

