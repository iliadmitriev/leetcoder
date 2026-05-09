class Solution:
    def interpret(self, command: str) -> str:
        res = []

        for ch in command:
            if ch == ")":
                if res[-1] == "(":
                    res.pop()
                    res.append("o")
                else:
                    res.pop()
                    res.pop()
                    res.pop()
                    res.append("al")
            else:
                res.append(ch)

        return "".join(res)

