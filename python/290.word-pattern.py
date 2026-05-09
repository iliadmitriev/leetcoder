class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(words) != len(pattern):
            return False

        fwd, back = {}, {}

        for char, word in zip(pattern, words):
            if word in fwd:
                if fwd[word] != char:
                    return False
            else:
                fwd[word] = char

            if char in back:
                if back[char] != word:
                    return False
            else:
                back[char] = word
                    
        return True