class Solution:
    def calPoints(self, operations: list[str]) -> int:
        line: list[int] = []

        for op in operations:
            if op == "+":
                line.append(line[-1] + line[-2])
            elif op == "D":
                line.append(2 * line[-1])
            elif op == "C":
                _ = line.pop()
            else:
                line.append(int(op))

        return sum(line)

