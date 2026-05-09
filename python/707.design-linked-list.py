from typing import Optional


class ListNode:
    __slots__ = (
        "val",
        "prev",
        "next",
    )

    def __init__(self, val=-1, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}, {self.next if self.next else 'x'}"


class MyLinkedList:

    def __init__(self) -> None:
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self.size = 0

    def _add_between(
        self, node: ListNode, prev: Optional[ListNode], next: Optional[ListNode]
    ) -> None:
        node.prev = prev
        node.next = next

        if prev:
            prev.next = node
        else:
            self.head = node

        if next:
            next.prev = node
        else:
            self.tail = node

        self.size += 1

    def _del_node(self, node: ListNode) -> None:
        prev = node.prev
        next = node.next

        if prev:
            prev.next = next
        else:
            self.head = next

        if next:
            next.prev = prev
        else:
            self.tail = prev

        self.size -= 1

    def _get(self, index: int) -> Optional[ListNode]:

        from_head = index < self.size // 2

        if from_head:
            cursor = self.head
            step = "next"
        else:
            cursor = self.tail
            index = self.size - 1 - index
            step = "prev"

        while index and cursor:
            index -= 1
            cursor = getattr(cursor, step, None)

        return cursor

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        res = self._get(index)
        return res.val if res else -1

    def addAtHead(self, val: int) -> None:
        self._add_between(ListNode(val), None, self.head)

    def addAtTail(self, val: int) -> None:
        self._add_between(ListNode(val), self.tail, None)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        if index <= 0:
            return self.addAtHead(val)

        if index == self.size:
            return self.addAtTail(val)

        pos = self._get(index)
        if not pos:
            return

        self._add_between(ListNode(val), pos.prev, pos)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        pos = self._get(index)
        if not pos:
            return

        self._del_node(pos)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)