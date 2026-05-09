
#include <vector>

using std::vector;

class Solution {
private:
  void dfs(TreeNode *node, vector<int> &path, int target,
           vector<vector<int>> &res) {
    if (!node) {
      return;
    }

    target -= node->val;
    path.push_back(node->val);

    if (!node->left && !node->right && target == 0) {
      res.push_back(path);
    }

    dfs(node->left, path, target, res);
    dfs(node->right, path, target, res);

    path.pop_back();
  }

public:
  vector<vector<int>> pathSum(TreeNode *root, int targetSum) {
    vector<vector<int>> res;
    vector<int> path;

    dfs(root, path, targetSum, res);

    return res;
  }
};