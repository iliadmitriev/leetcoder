# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        while True:
            r = (rand7() - 1) * 7 + rand7() - 1

            if r < 40:
                return r % 10 + 1
        