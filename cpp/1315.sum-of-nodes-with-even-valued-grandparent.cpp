/**
 * Definition for a binary tree node.
 */
class Solution {
public:
  int sumEvenGrandparent(TreeNode *root) {
    if (!root) {
      return 0;
    }

    stack<tuple<TreeNode *, TreeNode *, TreeNode *>> st;
    st.push({root, nullptr, nullptr});

    int res = 0;

    while (!st.empty()) {
      auto [node, parent, grandParent] = st.top();
      st.pop();

      if (grandParent && grandParent->val % 2 == 0) {
        res += node->val;
      }

      if (node->left) {
        st.push({node->left, node, parent});
      }

      if (node->right) {
        st.push({node->right, node, parent});
      }
    }

    return res;
  }
};