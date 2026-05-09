

class Solution:
    def robotWithString(self, s: str) -> str:
        stack = []

        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        res = []
        i = 0

        for c in range(26):
            # pop all the chars from stack that are less than or equal to current char
            while stack and stack[-1] <= c:
                res.append(chr(stack.pop() + ord("a")))

            # move forward and print all met current chars
            # all other chars add to stack
            while count[c] > 0:
                count[ord(s[i]) - ord("a")] -= 1

                if ord(s[i]) - ord("a") != c:
                    stack.append(ord(s[i]) - ord("a"))
                else:
                    res.append(s[i])

                i += 1

        while stack:
            res.append(chr(stack.pop() + ord("a")))

        return "".join(res)

