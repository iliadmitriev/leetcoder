// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }

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
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let (mut mid, mut end) = (&head, &head);
        let mut res = 0;
        let mut stack = Vec::new();

        while let Some(ListNode {
            next: Some(fast), ..
        }) = end.as_deref()
        {
            end = &fast.next;

            if let Some(slow) = mid.as_deref() {
                stack.push(slow.val);
                mid = &slow.next;
            }
        }

        while let (Some(node), Some(val)) = (mid.as_deref(), stack.pop()) {
            mid = &node.next;

            res = res.max(node.val + val);
        }

        res
    }
}
