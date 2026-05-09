class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        """
        Time: O(1)
        Space: O(1)

        1. Calculate the sum of all numbers from 1 to n.
        2. Calculate the sum of all numbers from 1 to n that are divisible by m.
        3. Return the difference between the two sums.

        S = 1 * m + 2 * m + 3 * m + ... + n

        m * (1 + 2 + 3 + ... + n // m)

        k = n // m

        1 .. k

        D = k * (k + 1) // 2

        S = D * m = k * (k + 1) // 2 * m

        Args:
            n (int): The maximum number in the range.
            m (int): The divisor.

        Returns:
            int: The difference between the sum of all numbers from 1 to n and
                 the sum of all numbers from 1 to n that are divisible by m.
        """
        num1 = (n * (n + 1)) // 2
        k = n // m
        num2 = (k * (k + 1)) // 2 * m

        return num1 - 2 * num2

