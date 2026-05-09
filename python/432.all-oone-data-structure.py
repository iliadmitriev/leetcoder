

class ListNode:
    __slots__ = (
        "next",
        "prev",
        "freq",
        "keys",
    )

    def __init__(
        self,
        freq: int,
        keys: set[str] | None = None,
        _next: "ListNode | None" = None,
        _prev: "ListNode | None" = None,
    ) -> None:
        if not keys:
            keys = set()

        self.freq = freq
        self.keys: set[str] = keys
        self.next, self.prev = _next, _prev


class AllOne:
    def __init__(self):
        self.head = ListNode(0)  # Dummy head
        self.tail = ListNode(0)  # Dummy tail
        self.head.next = self.tail  # Link dummy head to dummy tail
        self.tail.prev = self.head  # Link dummy tail to dummy head
        self.map: dict[str, ListNode] = {}  # Mapping from key to its node

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)  # Remove key from current node

            nextNode = node.next
            assert nextNode

            if nextNode == self.tail or nextNode.freq != freq + 1:
                # Create a new node if next node does not exist or freq is not freq + 1
                newNode = ListNode(freq + 1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:
                # Increment the existing next node
                nextNode.keys.add(key)
                self.map[key] = nextNode

            # Remove the current node if it has no keys left
            if not node.keys:
                self.removeNode(node)
        else:  # Key does not exist
            firstNode = self.head.next
            assert firstNode

            if firstNode == self.tail or firstNode.freq > 1:
                # Create a new node
                newNode = ListNode(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                self.head.next = newNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode

    def dec(self, key: str) -> None:
        if key not in self.map:
            return  # Key does not exist

        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.map[key]
        else:
            prevNode = node.prev
            assert prevNode

            if prevNode == self.head or prevNode.freq != freq - 1:
                newNode = ListNode(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                # Decrement the existing previous node
                prevNode.keys.add(key)
                self.map[key] = prevNode

        # Remove the node if it has no keys left
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""  # No keys exist
        assert self.tail.prev

        return next(
            iter(self.tail.prev.keys)
        )  # Return one of the keys from the tail's previous node

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""  # No keys exist
        assert self.head.next

        return next(
            iter(self.head.next.keys)
        )  # Return one of the keys from the head's next node

    def removeNode(self, node: ListNode) -> None:
        prevNode = node.prev
        nextNode = node.next

        assert prevNode and nextNode

        prevNode.next = nextNode  # Link previous node to next node
        nextNode.prev = prevNode  # Link next node to previous node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()