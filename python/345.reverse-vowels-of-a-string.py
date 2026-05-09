class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        while left < right:
            # 1. move left pointer to next wovel
            while left < right and s[left] not in vowels:
                left += 1
            # 2. move right pointer to next wovel
            while left < right and s[right] not in vowels:
                right -= 1
            # 3. swap values
            s[left], s[right] = s[right], s[left]
            # 4. move pointers ahead one step
            left += 1
            right -= 1
        
        return "".join(s)