class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        DFS approach.

        0. build hash set of words (for O(1) lookup)
        1. for every word, iterate its possible suffixes and prefixes "word" -> [("w", "ord"), ("wo", "rd"), ("wor", "d")]
        2. check if prefix is exists than two possible situations:
            2.1 suffix also exists -> word is concatenation of words (return true)
            2.2 repeat step 1 for suffix (return true)
        """
        words_hash_set = set(words)

        @cache
        def dfs(substr: str) -> bool:
            for i in range(1, len(substr)):
                prefix = substr[:i]
                suffix = substr[i:]
                if prefix in words_hash_set:
                    if suffix in words_hash_set or dfs(suffix):
                        return True
            return False

        return [word for word in words if dfs(word)]
