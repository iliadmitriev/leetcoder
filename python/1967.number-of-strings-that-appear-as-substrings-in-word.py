class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def check(pat: str, word: str) -> bool:
            return word.find(pat) != -1


        return sum(check(pat, word) for pat in patterns) 
        