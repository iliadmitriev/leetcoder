

class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:
        counter = 0
        ptr = head

        while ptr:
            counter += 1
            ptr = ptr.next

        parts = [None] * k

        full = counter // k
        partial = counter % k

        ptr, prev = head, None

        for i in range(k):
            parts[i] = ptr

            count = full
            if partial > 0:
                count += 1
                partial -= 1

            while count > 0:
                prev = ptr
                ptr = ptr.next
                count -= 1

            if prev:
                prev.next = None

        return parts

