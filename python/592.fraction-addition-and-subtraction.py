class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def fractionAddition(self, expression: str) -> str:
        frac: list[tuple[int, int, int]] = []

        i, j = 0, 0
        if expression[j] == "-":
            j += 1

        while j < len(expression):
            while j < len(expression) and expression[j] != "+" and expression[j] != "-":
                j += 1

            sign = -1 if expression[i] == "-" else 1
            if sign < 0:
                i += 1

            data = expression[i:j].split("/")
            frac.append((sign, int(data[0]), int(data[1])))
            i = j
            j = i + 1

        sign, num, den = 1, 0, 1

        for _sign, _num, _den in frac:
            num = sign * num * _den + _sign * _num * den
            sign = -1 if num < 0 else 1
            den *= _den
            num *= sign

        if num == 0:
            return "0/1"

        signStr = "" if sign == 1 else "-"

        g = self.gcd(num, den)
        num //= g
        den //= g

        return f"{signStr}{num}/{den}"

