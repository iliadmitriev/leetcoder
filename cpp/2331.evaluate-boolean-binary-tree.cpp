
class Solution {
public:
  bool evaluateTree(TreeNode *root) {
    if (!root) {
      return false;
    }

    if (!root->left && !root->right) {
      return root->val == 1;
    }

    if (root->val == 2) {
      return evaluateTree(root->left) || evaluateTree(root->right);
    }

    if (root->val == 3) {
      return evaluateTree(root->left) && evaluateTree(root->right);
    }

    return false;
  }
};