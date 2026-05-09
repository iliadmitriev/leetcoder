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
use std::cmp::Ordering;
use std::mem::drop;
use std::rc::Rc;

type TreeNodeRef = Rc<RefCell<TreeNode>>;

impl Solution {
    pub fn subtree_with_all_deepest(root: Option<TreeNodeRef>) -> Option<TreeNodeRef> {
        Self::dfs(root, 0).0
    }

    fn dfs(node: Option<TreeNodeRef>, depth: i32) -> (Option<TreeNodeRef>, i32) {
        if let Some(node_rc) = node {
            let node_ref = node_rc.borrow();
            let (left, left_depth) = Self::dfs(node_ref.left.clone(), depth + 1);
            let (right, right_depth) = Self::dfs(node_ref.right.clone(), depth + 1);
            drop(node_ref); // release borrow

            match (left, right) {
                (None, None) => (Some(node_rc), depth),
                (Some(left_node), None) => (Some(left_node), left_depth),
                (None, Some(right_node)) => (Some(right_node), right_depth),
                (Some(left_node), Some(right_node)) => match left_depth.cmp(&right_depth) {
                    Ordering::Greater => (Some(left_node), left_depth),
                    Ordering::Less => (Some(right_node), right_depth),
                    Ordering::Equal => (Some(node_rc), left_depth),
                },
            }
        } else {
            (None, 0)
        }
    }
}