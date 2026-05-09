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
use std::rc::Rc;

const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut subtree = Vec::new();
        Self::get_subtree_sum(root, &mut subtree);

        let total = *subtree.last().unwrap_or(&0);

        let max_product = subtree
            .iter()
            .map(|&sum| sum * (total - sum))
            .max()
            .unwrap_or(0);

        (max_product % MOD) as i32
    }

    fn get_subtree_sum(node: Option<Rc<RefCell<TreeNode>>>, sums: &mut Vec<i64>) -> i64 {
        if let Some(node_rc) = node {
            let node_ref = node_rc.borrow();
            let left = Self::get_subtree_sum(node_ref.left.clone(), sums);
            let right = Self::get_subtree_sum(node_ref.right.clone(), sums);
            let total = node_ref.val as i64 + left + right;

            sums.push(total % MOD);
            total
        } else {
            0
        }
    }
}