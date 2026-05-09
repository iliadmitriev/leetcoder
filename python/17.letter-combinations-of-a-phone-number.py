class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        if digits:
            res = list(mp[digits[0]])
        else:
            res = []

        for digit in digits[1:]:
            tmp = []
            for ch in mp[digit]:
                for head in res:
                    tmp.append(head + ch)
            res = tmp

        return res
