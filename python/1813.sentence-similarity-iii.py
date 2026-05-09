

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        words1, words2 = sentence1.split(), sentence2.split()
        len1, len2 = len(words1), len(words2)

        if len1 > len2:
            len1, len2 = len2, len1
            words1, words2 = words2, words1

        start = 0
        while start < len1 and words1[start] == words2[start]:
            start += 1

        end1, end2 = len1 - 1, len2 - 1
        while end1 >= start and words1[end1] == words2[end2]:
            end1 -= 1
            end2 -= 1

        return start > end1

