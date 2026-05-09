class Spreadsheet:
    def __init__(self, rows: int):
        self.data = {}

    def _formula(self, formula: str) -> tuple[str, str]:
        """Convert formula `=A1+B2` to `(A1, B2)`."""
        _, ops = formula.split("=")
        op1, op2, *_ = ops.split("+")
        return op1, op2

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        self.data.pop(cell, None)

    def getValue(self, formula: str) -> int:
        op1, op2 = self._formula(formula)

        if op1.isdigit():
            v1 = int(op1)
        else:
            v1 = self.data.get(op1, 0)

        if op2.isdigit():
            v2 = int(op2)
        else:
            v2 = self.data.get(op2, 0)

        return v1 + v2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)