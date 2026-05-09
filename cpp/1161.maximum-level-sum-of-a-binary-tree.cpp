
class Solution {
public:
  int maxLevelSum(TreeNode *root) {
    if (!root) {
      return 0;
    }

    int maxLevel = 1, level = 1, maxSum = root->val;
    queue<TreeNode *> q;
    q.push(root);

    while (q.size()) {
      int cur = 0;

      for (int size = q.size(); size; size--) {
        TreeNode *node = q.front();
        q.pop();

        cur += node->val;

        if (node->left) {
          q.push(node->left);
        }

        if (node->right) {
          q.push(node->right);
        }
      }

      if (maxSum < cur) {
        maxLevel = level;
        maxSum = cur;
      }
      level++;
    }

    return maxLevel;
  }
};
