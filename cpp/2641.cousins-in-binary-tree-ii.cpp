class Solution {
public:
  TreeNode *replaceValueInTree(TreeNode *root) {
    if (!root) {
      return root;
    }

    queue<TreeNode *> q{{root}};
    int prevLevelSum = root->val;

    while (q.size()) {
      int size = q.size();
      int levelSum = 0;

      while (size--) {
        auto node = q.front();
        q.pop();

        node->val = prevLevelSum - node->val;

        int brothers = (node->left ? node->left->val : 0) +
                       (node->right ? node->right->val : 0);

        if (node->left) {
          levelSum += node->left->val;
          node->left->val = brothers;
          q.push(node->left);
        }

        if (node->right) {
          levelSum += node->right->val;
          node->right->val = brothers;
          q.push(node->right);
        }
      }

      prevLevelSum = levelSum;
    }

    return root;
  }
};