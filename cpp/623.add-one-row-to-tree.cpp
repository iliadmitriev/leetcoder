/**
 * Definition for a binary tree node.
 */

#include <queue>

using namespace std;

// struct TreeNode {
//   int val;
//   TreeNode *left;
//   TreeNode *right;
//   TreeNode() : val(0), left(nullptr), right(nullptr) {}
//   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//   TreeNode(int x, TreeNode *left, TreeNode *right)
//       : val(x), left(left), right(right) {}
// };

class Solution {
private:
  TreeNode *dfs(TreeNode *root, int val, int depth, int currDepth) {
    if (!root) {
      return nullptr;
    }

    if (depth - 1 == currDepth) {
      root->left = new TreeNode(val, root->left, nullptr);
      root->right = new TreeNode(val, nullptr, root->right);
    } else if (depth > currDepth) {
      root->left = dfs(root->left, val, depth, currDepth + 1);
      root->right = dfs(root->right, val, depth, currDepth + 1);
    }

    return root;
  }

public:
  TreeNode *addOneRow(TreeNode *root, int val, int depth) {
    if (depth == 1) {
      return new TreeNode(val, root, nullptr);
    }

    return dfs(root, val, depth, 1);
  }
};