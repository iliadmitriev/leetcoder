class Solution {
public:
  TreeNode *reverseOddLevels(TreeNode *root) {
    if (!root) {
      return root;
    }

    deque<TreeNode *> q;
    q.push_back(root);

    int level = 0;

    while (q.size()) {
      if (level % 2) {
        for (int i = 0, j = q.size() - 1; i < j; i++, j--) {
          std::swap(q[i]->val, q[j]->val);
        }
      }

      for (int i = q.size(); i; i--) {
        TreeNode *node = q.front();
        q.pop_front();

        if (node->left) {
          q.push_back(node->left);
        }

        if (node->right) {
          q.push_back(node->right);
        }
      }

      level++;
    }

    return root;
  }
};