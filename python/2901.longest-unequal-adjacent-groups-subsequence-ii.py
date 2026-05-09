class Solution:
    def getWordsInLongestSubsequence(
        self, words: list[str], groups: list[int]
    ) -> list[str]:
        n = len(words)

        def hamming_distance(s1, s2):
            count = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    count += 1
            return count

        dp = [1 * n for _ in range(n)]
        prev = [-1] * n

        max_len = 1
        end = 0

        for i in range(n):
            for j in range(i):
                if (
                    groups[i] == groups[j]
                    or len(words[i]) != len(words[j])
                    or hamming_distance(words[i], words[j]) != 1
                ):
                    continue

                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                end = i

        res = []
        i = end
        while i != -1:
            res.append(words[i])
            i = prev[i]

        return res[::-1]

