// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut queue = VecDeque::new();
        if let Some(node) = root {
            queue.push_back(node);
        } else {
            return 0;
        }

        let mut max_level = 1;
        let mut max_sum = i32::MIN;
        let mut level = 1;

        while !queue.is_empty() {
            let level_size = queue.len();
            let mut current_sum = 0;

            for _ in 0..level_size {
                let node = queue.pop_front().unwrap();
                let node_ref = node.borrow();

                current_sum += node_ref.val;

                if let Some(left) = node_ref.left.clone() {
                    queue.push_back(left);
                }

                if let Some(right) = node_ref.right.clone() {
                    queue.push_back(right);
                }
            }

            if current_sum > max_sum {
                max_sum = current_sum;
                max_level = level;
            }

            level += 1;
        }

        max_level
    }
}