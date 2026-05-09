class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        fwd = x
        while x:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        return fwd == rev
