from collections.abc import Iterator


class Solution:
    def tokenize(self, s: str) -> Iterator[str]:
        i = 0
        while i < len(s):
            if s[i] == "(":
                yield "("
                i += 1
            elif s[i] == ")":
                yield ")"
                i += 1
            elif s[i].isalpha():
                j = i + 1
                while j < len(s) and s[j].isalpha() and s[j].islower():
                    j += 1
                yield s[i:j]
                i = j
            elif s[i].isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                yield s[i:j]
                i = j

    def flatten(self, st: list[dict[str, int]]) -> dict[str, int]:
        res: dict[str, int] = {}
        while st and st[-1]:
            s = st.pop()
            for k, v in s.items():
                res[k] = res.get(k, 0) + v
        _ = st.pop() if st else None
        return res

    def countOfAtoms(self, formula: str) -> str:

        stack: list[dict[str, int]] = []

        for c in self.tokenize(formula):

            if c == "(":
                stack.append({})
            elif c == ")":
                cur = self.flatten(stack)
                stack.append(cur)
            elif c.isalpha():
                stack.append({c: 1})
            elif c.isdigit():
                count = int(c)
                cur = stack[-1]
                for k in cur.keys():
                    cur[k] *= count

        tmp = self.flatten(stack)
        res: list[str] = []
        for k, v in sorted(tmp.items()):
            res.append(f"{k}" if v == 1 else f"{k}{v}")

        return "".join(res)

