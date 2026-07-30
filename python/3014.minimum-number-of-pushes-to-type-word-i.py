class Solution:
    def minimumPushes(self, word: str) -> int:
        
        cnt = [0] * 26
        base = ord("a")
        for ch in word:
            cnt[ord(ch) - base] += 1

        res = 0
        push = 0

        for k, c in enumerate(sorted(filter(None, cnt), reverse=True)):
            # the first 8 most frequest letters 
            # is be added as the first button positions
            if k % 8 == 0:
                push += 1

            res += c * push


        return res
        