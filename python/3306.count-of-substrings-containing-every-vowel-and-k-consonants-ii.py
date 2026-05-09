from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atleast(k):
            vowel = defaultdict(int)
            non_vowel = 0
            counter = 0
            left = 0

            for right in range(len(word)):
                if word[right] in "aeiou":
                    vowel[word[right]] += 1
                else:
                    non_vowel += 1

                while len(vowel) == 5 and non_vowel >= k:
                    counter += len(word) - right

                    if word[left] in "aeiou":
                        vowel[word[left]] -= 1

                        if vowel[word[left]] == 0:
                            del vowel[word[left]]

                    else:
                        non_vowel -= 1

                    left += 1

            return counter

        return atleast(k) - atleast(k + 1)

