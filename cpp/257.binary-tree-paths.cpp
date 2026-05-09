
#include <string>
#include <vector>

using std::string;
using std::to_string;
using std::vector;

class Solution {
private:
  void dfs(TreeNode *node, string path, vector<string> &res) {
    if (!node) {
      return;
    }

    if (!node->left && !node->right) {
      res.push_back(path + to_string(node->val));
      return;
    }

    if (node->left) {
      dfs(node->left, path + to_string(node->val) + "->", res);
    }

    if (node->right) {
      dfs(node->right, path + to_string(node->val) + "->", res);
    }
  }

public:
  vector<string> binaryTreePaths(TreeNode *root) {
    vector<string> res;
    dfs(root, "", res);
    return res;
  }
};