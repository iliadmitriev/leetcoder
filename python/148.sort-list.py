# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self, ptr: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find middle of linked list and return it
        Uses two pointers fast(2x) and slow(1x)
    
        1 -> 2 -> 3 -> 4
             ^
             |
             middle
        
        """
        fast = slow = ptr
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two linked lists in one in ascending order
        """
        res = ptr = ListNode(-1)
        
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
                
            ptr = ptr.next
        
        ptr.next = list1 or list2
            
        return res.next
    
    
    def merge_sort(self, ptr: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge sort algorithm
        1) find middle (and split)
        2) run merge sort algorithm with two parts
        3) merge two sorted list in ascending order
        """
        if ptr is None or ptr.next is None:
            return ptr
        
        mid = self.find_mid(ptr)
        ptr2 = mid.next
        mid.next = None # cut in half
        
        # run merge sort with two lists
        res1 = self.merge_sort(ptr)
        res2 = self.merge_sort(ptr2)
        
        return self.merge(res1, res2)
    
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge_sort(head)    
        