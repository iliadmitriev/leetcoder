def cross(s, a, b) -> int:
    """Return cross product (area of parallelogram).

    Calculate cross product of two vectors set by 3 points.

    Args:
     s (int, int): x, y coords of start points of both vectors.
     a (int, int): x, y coords of end of point vector a.
     b (int, int): x, y coords of end of point vector b.

    Returns:
      cross product.
    """
    # calculate vector coordinates
    v = a[0] - s[0], a[1] - s[1]
    w = b[0] - s[0], b[1] - s[1]
    # a * d - b * c
    return v[0] * w[1] - v[1] * w[0]


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        def fence(points: List[List[int]]) -> List[List[int]]:
            stack = []
            for p in points:
                while len(stack) >= 2 and cross(stack[-2], stack[-1], p) > 0:
                    stack.pop(-1)
                stack.append(tuple(p))

            return stack

        trees.sort()
        up_dir_fence = fence(trees)
        down_dir_fence = fence(trees[::-1])

        return set(up_dir_fence + down_dir_fence)




