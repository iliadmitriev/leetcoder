
class Solution {
private:
  std::pair<TreeNode *, int> dfs(TreeNode *node, int depth) {
    if (!node) {
      return {nullptr, 0};
    }

    auto [left, left_depth] = dfs(node->left, depth + 1);
    auto [right, right_depth] = dfs(node->right, depth + 1);

    if (!left && !right) {
      return {node, depth};
    }

    if (left_depth > right_depth) {
      return {left, left_depth};
    } else if (left_depth < right_depth) {
      return {right, right_depth};
    }

    return {node, left_depth};
  };

public:
  TreeNode *lcaDeepestLeaves(TreeNode *root) { return dfs(root, 0).first; }
};