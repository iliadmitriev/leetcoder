class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                left, right = stack.pop(), stack.pop()

                if abs(left) == abs(right):
                    continue
                elif abs(left) < abs(right):
                    stack.append(right)
                else:
                    stack.append(left)

        return stack
