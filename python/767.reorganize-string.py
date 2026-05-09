class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)

        max_count, letter = 0, ''

        letter = max(char_count.keys(), key=char_count.get)
        max_count = char_count[letter]

        if max_count > (len(s) + 1) // 2:
            return ""
        
        ans = [''] * len(s)
        index = 0

        # put most frequest
        while char_count[letter] != 0:
            ans[index] = letter
            index += 2
            char_count[letter] -= 1

        # put the rest of letters
        for char, count in char_count.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1

        return ''.join(ans)