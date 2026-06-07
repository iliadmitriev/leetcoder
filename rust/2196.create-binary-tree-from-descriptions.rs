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
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut tree: HashMap<i32, Rc<RefCell<TreeNode>>> = HashMap::new();
        let mut has_parent: HashSet<i32> = HashSet::new();

        for edge in &descriptions {
          let (parent, child, is_left) = (edge[0], edge[1], edge[2] == 1);

          has_parent.insert(child);

          let parent_node = tree
            .entry(parent)
            .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(parent))))
            .clone();

          let child_node = tree
            .entry(child)
            .or_insert_with(|| Rc::new(RefCell::new(TreeNode::new(child))))
            .clone();

          if is_left {
            parent_node.borrow_mut().left = Some(child_node);
          } else {
            parent_node.borrow_mut().right = Some(child_node);
          }
        }

        for edge in &descriptions {
          let parent = edge[0];

          if !has_parent.contains(&parent) {
            return tree.get(&parent).cloned();
          }
        }

        None
    }
}