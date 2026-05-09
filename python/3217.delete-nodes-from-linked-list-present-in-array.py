

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        res = ListNode()
        numsSet = set(nums)

        h = res

        while head:
            if head.val not in numsSet:
                h.next = head
                h = h.next
            head = head.next

        h.next = None

        return res.next

