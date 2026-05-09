# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(num: Optional[ListNode]):
            res = 0
            while num:
                res = 10 * res + num.val
                num = num.next
            return res
        
        def get_list(num: int):
            node = None
            while num:
                num, digit = divmod(num, 10)
                node = ListNode(digit, node)

            return node if node else ListNode()

        num1, num2 = get_num(l1), get_num(l2)
        return get_list(num1 + num2)

