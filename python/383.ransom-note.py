class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        letters = Counter(magazine)
        
        for sign in note.keys():
            if sign not in letters or letters[sign] < note[sign]:
                return False
        return True