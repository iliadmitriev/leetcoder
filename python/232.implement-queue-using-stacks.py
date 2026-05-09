class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def _move(self):
        """Fill output.
        Time: O(n)

        Will work only if output is empty.
        Get all values from input stack in reversed order
        and put them to output stack.
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def push(self, x: int) -> None:
        """Push value to input.
        
        Time: O(1)
        """
        self.input.append(x)

    def pop(self) -> int:
        """Pop value from output.

        Pop value from output (Time: O(1))
        If output is empty, fill output from input. (O(n))
        """
        self._move()
        return self.output.pop()

    def peek(self) -> int:
        """Peek value from output.
        
        Peek value from output (Time: O(1))
        If output is empty, fill output from input. (O(n))
        """
        self._move()
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()