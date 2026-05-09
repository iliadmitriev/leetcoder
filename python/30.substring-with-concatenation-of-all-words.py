class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        m = len(words)
        word_len = len(words[0])
        sub_size = word_len * m
        words_count = Counter(words)
        
        def dp(i: int) -> bool:
            remaining = words_count.copy()
            words_used = 0
            
            for j in range(i, i + sub_size, word_len):
                sub = s[j: j + word_len]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break
            
            return words_used == m
        
        res = []
        for i in range(n - word_len + 1):
            if dp(i):
                res.append(i)
        return res