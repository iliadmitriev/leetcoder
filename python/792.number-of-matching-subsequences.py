class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # store word positions for every word
        # starting from 0 (beggining of word)
        word_pos = [0] * len(words)
        # map from letter to list word indexes
        letter_idx = defaultdict(list)
        # add list of word indexes for every first letters
        for i, word in enumerate(words):
            letter_idx[word[0]].append(i)
        
        # result count
        res = 0
        
        # iterate all chars from input string
        for ch in s:
            # skip if char not found
            if ch not in letter_idx:
                continue
            # get current char word indexes
            indexes = letter_idx.pop(ch)
            # iterate all word indexes
            for idx in indexes:
                # shift word positions for word index
                word_pos[idx] += 1
                # check if we have reached end of the word
                if word_pos[idx] == len(words[idx]):
                    # increase result count
                    res += 1
                elif word_pos[idx] < len(words[idx]):
                    # append new index to next letter indexes
                    letter_idx[words[idx][word_pos[idx]]].append(idx)
                               
        return res