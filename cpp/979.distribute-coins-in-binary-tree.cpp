
class Solution {
public:
  int distributeCoins(TreeNode *root) {
    int res = 0;

    std::function<int(TreeNode *)> dfs;
    dfs = [&res, &dfs](TreeNode *node) -> int {
      if (!node)
        return 0;

      auto left = dfs(node->left);
      auto right = dfs(node->right);

      res += std::abs(left) + std::abs(right);

      return node->val + left + right - 1;
    };

    dfs(root);

    return res;
  }
};