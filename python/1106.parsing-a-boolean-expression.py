class Solution:

    @staticmethod
    def eval(st: list[bool | str], op: str) -> bool:
        if op == "!":
            res = False
            while st and isinstance(st[-1], bool):
                res = not st.pop()
            return res
        elif op == "&":
            res = True
            while st and isinstance(st[-1], bool):
                res = bool(st.pop()) and res
            return res
        elif op == "|":
            res = False
            while st and isinstance(st[-1], bool):
                res = bool(st.pop()) or res
            return res
        else:
            raise ValueError

    def parseBoolExpr(self, expression: str) -> bool:

        stack = []
        op = "x"

        for tok in expression:

            if tok == ",":
                continue

            if tok in ("!", "&", "|"):
                stack.append(op)
                op = tok

            elif tok == "(":
                pass

            elif tok == ")":
                val = self.eval(stack, op)
                op = stack.pop()
                stack.append(val)

            else:

                if tok == "t":
                    stack.append(True)
                elif tok == "f":
                    stack.append(False)

        return stack.pop()

