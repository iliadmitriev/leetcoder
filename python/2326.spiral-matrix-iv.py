class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode | None) -> list[list[int]]:
        def linked_list_gen(node: ListNode | None) -> Iterator[int]:

            while node:
                yield node.val
                node = node.next

            while True:
                yield -1

        left, right, top, bottom = 0, n - 1, 0, m - 1
        nodes = linked_list_gen(head)
        res = [[-1] * n for _ in range(m)]

        while top < bottom and left < right:
            for i in range(left, right):
                res[top][i] = next(nodes)

            for i in range(top, bottom):
                res[i][right] = next(nodes)

            for i in range(right, left, -1):
                res[bottom][i] = next(nodes)

            for i in range(bottom, top, -1):
                res[i][left] = next(nodes)

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        for i in range(left, right + 1):
            for j in range(top, bottom + 1):
                res[j][i] = next(nodes)

        return res

