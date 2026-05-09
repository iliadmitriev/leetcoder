from functools import reduce
import operator

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def mask_word(s: str) -> int:
            """Build word bitmask.
            
            Convert word to OR bitmask of it's letters.
            'a' => 1 << 0
            'b' => 1 << 1
            ...
            'z' => 1 << 26
            
            Args:
                s (str): given string
            Returns:
                (int): bitmask
            """
            return reduce(operator.or_, map(lambda x: 1 << (ord(x) - ord('a')), s), 0)
        
        # build map:
        # bitmask -> maximum word length
        mask = dict()
        for w in words:
            key = mask_word(w)
            mask[key] = max(mask.get(key, 0), len(w))
        
        return max(
            [
                mask[a] * mask[b] for a in mask for b in mask
                if not a & b
            ] or [0]
        )