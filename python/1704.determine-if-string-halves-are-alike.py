class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiou')
        a = sum(char.lower() in vowels for char in s[:len(s) // 2])
        b = sum(char.lower() in vowels for char in s[len(s) // 2:])

        return a == b
         