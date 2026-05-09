from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0

        cnt = defaultdict(int)
        cnt[0] = 1

        for c in word:
            mask ^= 1 << (ord(c) - 97)
            cnt[mask] += 1

        res = 0
        for mask, count in cnt.items():
            res += count * (count - 1) // 2
            for i in range(10):
                mask2 = mask ^ (1 << i)
                if mask2 < mask:
                    res += count * cnt.get(mask2, 0)

        return res

