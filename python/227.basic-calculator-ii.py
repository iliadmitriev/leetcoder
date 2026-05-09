class Solution:
    def calculate(self, s: str) -> int:
        n = 0
        s += '+'
        stack = []
        operation = '+'
        for ch in s:
            if ch.isdigit():
                n = n * 10 + int(ch)
            elif ch in '+-*/':
                if operation == '+':
                    stack.append(n)
                elif operation == '-':
                    stack.append(-n)
                elif operation == '*':
                    stack.append(stack.pop() * n)
                elif operation == '/':
                    stack.append(int(stack.pop() / n))
                operation = ch
                n = 0
                
        return sum(stack)