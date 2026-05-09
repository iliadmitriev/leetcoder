class RingBufferNode:
    slots = ("prev", "next", "value")

    def __init__(
        self,
        value: int,
        next: "RingBufferNode | None" = None,
        prev: "RingBufferNode | None" = None,
    ):
        self.value = value
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.front: RingBufferNode | None = None
        self.last: RingBufferNode | None = None

    def insert(self, value: int) -> RingBufferNode:
        newNode = RingBufferNode(value, self.front, self.last)

        if self.isEmpty() or not self.front or not self.last:
            self.front, self.last = newNode, newNode
        else:
            self.front.prev, self.last.next = newNode, newNode

        return newNode

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = self.insert(value)
        self.size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.last = self.insert(value)
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty() or not self.front or not self.last:
            return False

        if self.front == self.last:
            self.front, self.last = None, None
        else:
            self.front = self.front.next

            if self.front:
                self.front.prev, self.last.next = self.last, self.front

        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty() or not self.front or not self.last:
            return False

        if self.front == self.last:
            self.front, self.last = None, None
        else:
            self.last = self.last.prev

            if self.last:
                self.last.next, self.front.prev = self.front, self.last

        self.size -= 1

        return True

    def getFront(self) -> int:
        if self.isEmpty() or not self.front:
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.isEmpty() or not self.last:
            return -1
        return self.last.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()