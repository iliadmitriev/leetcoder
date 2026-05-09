
#include <utility>
using std::pair;

class Solution {
public:
  TreeNode *subtreeWithAllDeepest(TreeNode *root) {
    auto [node, _] = dfs(root, 0);
    return node;
  }

private:
  pair<TreeNode *, int> dfs(TreeNode *node, int depth) {
    if (!node) {
      return {NULL, 0};
    }

    auto [left, leftDepth] = dfs(node->left, depth + 1);
    auto [right, rightDepth] = dfs(node->right, depth + 1);

    if (!left and !right) {
      return {node, depth};
    } else if (leftDepth > rightDepth) {
      return {left, leftDepth};
    } else if (rightDepth > leftDepth) {
      return {right, rightDepth};
    }

    return {node, leftDepth};
  }
};