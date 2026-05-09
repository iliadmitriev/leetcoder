class Solution:
    def partitionString(self, s: str) -> int:
        flag = 0
        count = 1
        for char in s:
            if (flag >> (ord(char) - 97)) & 1:
                count += 1
                flag = 0
            flag |= 1 << ord(char) - 97
        return count