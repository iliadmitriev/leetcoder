// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }


impl Solution {
    pub fn delete_middle(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Pass 1: Find the length of the linked list
        let mut len = 0;
        let mut curr = &head;
        while let Some(node) = curr {
            len += 1;
            curr = &node.next;
        }
        
        // If the list has 0 or 1 node, the middle node is the only node, so we return None
        if len <= 1 {
            return None;
        }
        
        // Pass 2: Traverse to the node just *before* the middle node
        let mut curr = &mut head;
        for _ in 0..(len / 2 - 1) {
            if let Some(node) = curr {
              curr = &mut node.next;
            }
        }
        
        // Remove the middle node by taking its `next` pointer
        if let Some(prev) = curr {
            if let Some(mid) = prev.next.take() {
                prev.next = mid.next;
            }
        }
        
        head
    }
}