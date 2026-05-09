/**
 * Definition for a binary tree node.
 */
// struct TreeNode {
//   int val;
//   TreeNode *left;
//   TreeNode *right;
//   TreeNode() : val(0), left(nullptr), right(nullptr) {}
//   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//   TreeNode(int x, TreeNode *left, TreeNode *right)
//       : val(x), left(left), right(right) {}
// };

#include <string>

using namespace std;

class Solution {
private:
  string smallestFromLeafUtil(TreeNode *root, string &str) {
    string val = char(97 + root->val) + str;
    if (!root->left && !root->right) {
      return val;
    }

    string left = root->left ? smallestFromLeafUtil(root->left, val) : "";
    string right = root->right ? smallestFromLeafUtil(root->right, val) : "";

    if (!left.size()) {
      return right;
    }

    if (!right.size()) {
      return left;
    }

    if (left < right) {
      return left;
    }

    return right;
  }

public:
  string smallestFromLeaf(TreeNode *root) {
    string str = "";
    return smallestFromLeafUtil(root, str);
  }
};