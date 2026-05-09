

class Solution:
    def postorder(self, node: "Node | None") -> list[int]:

        def postorder_it(node: "Node | None") -> Iterator[int]:
            if node is None:
                return

            if node.children:
                for child in node.children:
                    yield from postorder_it(child)

            yield node.val

        return list(postorder_it(node))

