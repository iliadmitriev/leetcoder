class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # dict of length -> list of words
        lengths = dict()
        for word in words:
            data = lengths.setdefault(len(word), [])
            data.append(word)

        cache = dict()
        res = 0
        # start from length = 1 up to 16 (inclusive)
        for l in range(1, 17):
            if l not in lengths:
                continue

            for word in lengths[l]:
                curr_max = 0
                for i in range(len(word)):
                    key = word[:i] + word[i + 1:]
                    curr_max = max(curr_max, cache.get(key, 0))

                cache[word] = 1 + curr_max

                res = max(res, cache[word])

        return res
