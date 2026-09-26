class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        res = []
        voc = dict(knowledge)
        j = 0

        for i in range(n + 1):
            if i == n or s[i] == '(':
                term = s[j: i]
                res.append(term)
                j = i + 1
            elif s[i] == ')':
                key = s[j: i]
                res.append(voc.get(key, '?'))
                j = i + 1

        return "".join(res)
        