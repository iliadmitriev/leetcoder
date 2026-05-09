class Solution:
    def mask(self, word: str) -> int:
        result = 0
        for ch in word:
            result |= 1 << (ord(ch)-ord('a'))
        return result

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        word_count = Counter(self.mask(word) for word in words)
        result = []
        for puzzle in puzzles:
            original_mask, first = self.mask(puzzle[1:]), self.mask(puzzle[0])
            curr_mask, count = original_mask, word_count[first]
            while curr_mask:
                count += word_count[curr_mask|first]
                curr_mask = (curr_mask-1)&original_mask
            result.append(count)
        return result
