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
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    fn dfs(node: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32, i32) {
        let node_rc = match node {
          Some(rc) => rc,
          None => return (0, 0, 0),
        };

        let (val, left, right) = {
          let node_ref = node_rc.borrow();

          (node_ref.val, node_ref.left.clone(), node_ref.right.clone())
        };


        let (left_matches, left_value, left_count) = Self::dfs(left);
        let (right_matches, right_value, right_count) = Self::dfs(right);

        let count = 1 + left_count + right_count;
        let value = val + left_value + right_value;
        let mut matches = left_matches + right_matches;

        if value / count == val {
          matches += 1;
        }

        (matches, value, count)
    }

    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
      let (res, _, _) = Solution::dfs(root);

      res
    }
}