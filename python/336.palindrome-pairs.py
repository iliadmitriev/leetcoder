class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        
        Idea:
        1. Build hashmap/trie of reversed words keys, storing their indexes as values
           (all words are unique by conditions, so their reversed counterparts should be the same unique)
        2. Iterate all words and check for 3 cases, adding word index to result
            
            case 1:
              if a word has it's mirrored copy in reverse index, i.e. 'abc' 'cba'

            case 2:
              if word is palindrome and there is and empty word
              they can be concatenated to palindrome
              i.e. 'abcba' ''

            case 3:
              if a word concatenated to a word from reversed index, can build palindrome:
              'cdcba' 'ab'
              'abcdc' 'ba'
        """
        # step 1: build reversed words index
        indexes = {}
        for i, word in enumerate(words):
            indexes[word[::-1]] = i
        
        res = []
        
        # step 2: iterate all words
        for i, word in enumerate(words):
            # case 1: a words has it's mirrored counterpart
            if word in indexes and indexes[word] != i:
                res.append((i, indexes[word]))
                
            # case 2: a word is not empty and is a palindrome by itself
            # and there is an empty word in indexes
            if word != '' and '' in indexes and word == word[::-1]:
                res.append((i, indexes['']))
                res.append((indexes[''], i))
                
            # case 3: a palindrome is concatenated of two different parts
            for j in range(len(word)):
                w1, w2 = word[j:], word[:j]
                if w1 in indexes and w2 == word[j - 1::-1]:
                    res.append((indexes[w1], i))
                if w2 in indexes and w1 == word[:j - 1:-1]:
                    res.append((i, indexes[w2]))
                
        return res