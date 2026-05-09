
class Solution {
public:
  bool isCousins(TreeNode *root, int x, int y) {
    if (!root) {
      return false;
    }

    queue<pair<TreeNode *, TreeNode *>> q;
    q.push({root, NULL});

    TreeNode *parentX, *parentY;

    while (!q.empty()) {
      parentX = NULL;
      parentY = NULL;
      for (int size = q.size(); size > 0; size--) {
        auto [node, parent] = q.front();
        q.pop();

        if (node->val == x) {
          parentX = parent;
        } else if (node->val == y) {
          parentY = parent;
        }

        if (parentX && parentY) {
          return parentX != parentY;
        }

        if (node->left) {
          q.push({node->left, node});
        }

        if (node->right) {
          q.push({node->right, node});
        }
      }
    }

    return false;
  }
};