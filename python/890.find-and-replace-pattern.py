class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def image(pat: str) -> List[int]:
            """Converts input string to list of indexes.
            
            'aaabbb' -> [1,1,1,2,2,2]
            'abc' -> [1,2,3]
            'nddk' -> [1,2,2,3]
            """
            mp = defaultdict(int)
            img = []
            index = 0
            for ch in pat:
                if ch not in mp:
                    index += 1
                    mp[ch] = index
                img.append(mp[ch])
            return img
        
        pattern_image = image(pattern)
        res = [word for word in words if pattern_image == image(word)]

        return res