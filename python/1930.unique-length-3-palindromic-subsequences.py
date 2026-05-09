class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0

        m = defaultdict(list)

        for i, ch in enumerate(s):
            m[ch].append(i)

        for ch in m.keys():
            if len(m[ch]) < 2:
                continue

            left = m[ch][0] + 1 # shift right by 1
            right = m[ch][-1]   # shift left by 1 (+1 -1)

            # cound unique symbols bounded beetween left and right 
            res += len(set(s[left: right]))

        return res