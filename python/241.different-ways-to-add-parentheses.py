

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:

        n = len(expression)
        dp: list[list[list[int]]] = [[[] for _ in range(n)] for _ in range(n)]
        self._init_base_cases(expression, dp)

        for length in range(3, n + 1):
            for start in range(n - length + 1):
                self._process_expression(expression, start, start + length - 1, dp)

        return dp[0][n - 1]

    def _init_base_cases(self, expression: str, dp: list[list[list[int]]]) -> None:
        for i in range(len(expression)):
            if expression[i].isdigit():
                dp[i][i].append(int(expression[i]))

                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    dp[i][i + 1].append(int(expression[i: i + 2]))

    def _process_expression(
        self, expression: str, start: int, end: int, dp: list[list[list[int]]]
    ) -> None:
        for split in range(start, end + 1):
            if expression[split].isdigit():
                continue

            leftResult = dp[start][split - 1]
            rightResult = dp[split + 1][end]

            dp[start][end].extend(
                self._compute(expression[split], leftResult, rightResult)
            )

    def _compute(self, op: str, left: list[int], right: list[int]) -> list[int]:

        results: list[int] = []
        for leftNum in left:
            for rightNum in right:
                if op == "+":
                    results.append(leftNum + rightNum)
                elif op == "-":
                    results.append(leftNum - rightNum)
                elif op == "*":
                    results.append(leftNum * rightNum)

        return results

