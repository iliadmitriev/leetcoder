class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = [0] * 26
        for c in word:
            cnt[ord(c) - ord("a")] += 1

        cnt.sort()

        # optimization: cut zeros
        j = 0
        while j < 26 and cnt[j] == 0:
            j += 1
        cnt = cnt[j:]

        minDeletions = sum(cnt)

        for x in cnt:
            cur = 0
            for v in cnt:
                if v < x:
                    cur += v
                else:
                    cur += max(0, v - (x + k))

            minDeletions = min(minDeletions, cur)

        return minDeletions

