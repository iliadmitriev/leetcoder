class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode | None) -> ListNode | None:

        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        curr = head
        while curr and curr.next:

            val = ListNode(gcd(curr.val, curr.next.val))
            curr.next, val.next, curr = val, curr.next, curr.next

        return head

