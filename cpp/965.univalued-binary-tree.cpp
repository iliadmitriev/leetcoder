
class Solution {
public:
  bool isUnivalTree(TreeNode *root) {
    stack<TreeNode *> q;
    q.push(root);
    int val = root->val;

    while (!q.empty()) {
      auto node = q.top();
      q.pop();

      if (val != node->val) {
        return false;
      }

      if (node->left) {
        q.push(node->left);
      }

      if (node->right) {
        q.push(node->right);
      }
    }

    return true;
  }
};
