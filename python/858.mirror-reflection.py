def gcd(x: int, y: int) -> int:
    """Finds the greatest common divisor.

    Uses euclidean method to find GCD.
    https://en.wikipedia.org/wiki/Euclidean_algorithm

    Args:
        x: first number
        y: second number

    Returns:
        (int): the greatest common divisor
    """

    while y:
        x, y = y, x % y
    return abs(x)


def lcm(a: int, b: int) -> int:
    """Find the least common multiple.

    Args:
        a: first number.
        b: second number.

    Returns:
        (int): The least common multiple.
    """
    return a * b // gcd(a, b)


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # don't need calculations (optimize)
        if p == q:
            return 1
        
        bounces = lcm(p, q)
        # if number of bounces divided by q is even
        # we end up in top left corner (2)
        print(bounces)
        if (bounces // q) % 2 == 0:
            return 2
        # number of bounces divided by p is even
        # then we end up in bottom right corner (0)
        # otherwise in top right corner (1)
        return (bounces // p) % 2