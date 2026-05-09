
class Solution {
public:
  int findSecondMinimumValue(TreeNode *root) {
    if (!root)
      return -1;

    int inf = -1;
    int first = inf;
    int second = inf;

    queue<TreeNode *> q;
    q.push(root);

    while (!q.empty()) {
      auto node = q.front();
      q.pop();

      if (node->val < first || first == inf) {
        second = first;
        first = node->val;
      } else if ((node->val < second || second == inf) && node->val != first) {
        second = node->val;
      }

      if (node->left) {
        q.push(node->left);
      }

      if (node->right) {
        q.push(node->right);
      }
    }

    return second == inf ? -1 : second;
  }
};