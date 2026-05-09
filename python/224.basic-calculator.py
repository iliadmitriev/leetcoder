class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        sign = 1
        num = 0
        stack = []
        for i, char in enumerate(s):
            # calculate current number for operation
            if char.isdigit():
                num = num * 10 + int(char)
            # if plus is pushed,
            # calculate current result and start new operation, setting sign to +1
            elif char == '+':
                total += num * sign
                sign = 1
                num = 0
            # if minus is pushed,
            # calculate current result and start new operation, setting sign to -1
            elif char == '-':
                total += num * sign
                sign = -1
                num = 0

            elif char == '(':
                # memorize current operation to stack
                stack.append((total, sign))
                # start off a new operation inside parentheses
                total = 0
                sign = 1
                num = 0

            elif char == ')':
                # finish pending operation inside parentheses
                num = total + num * sign
                # extract previous operation from stack, and continue calculation
                total, sign = stack.pop()

        return total + num * sign
