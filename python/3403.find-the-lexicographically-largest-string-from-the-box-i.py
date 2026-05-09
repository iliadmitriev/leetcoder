class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        win = n - numFriends + 1
        i = 0
        j = 1
        k = 0

        while j + k < n:

            if word[i + k] == word[j + k]:
                k += 1
            elif word[i + k] > word[j + k]:
                j = j + k + 1
                k = 0
            else:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0

        return word[i: i + win]

