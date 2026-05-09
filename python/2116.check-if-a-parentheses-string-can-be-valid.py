class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stack = []
        freeStack = []

        for i in range(len(s)):
            if locked[i] == "1":

                if s[i] == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    elif freeStack:
                        freeStack.pop()
                    else:
                        return False

            else:
                freeStack.append(i)

        while stack and freeStack:
            topFree = freeStack.pop()
            top = stack.pop()

            if topFree < top:
                return False

        return not stack and len(freeStack) % 2 == 0

