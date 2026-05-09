/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
#include <stack>

using namespace std;
class Solution {
public:
  int sumNumbers(TreeNode *root) {
    int res = 0;

    stack<pair<TreeNode *, int>> st;
    if (root) {
      st.push({root, 0});
    }

    while (!st.empty()) {
      auto [node, total] = st.top();
      st.pop();

      total = total * 10 + node->val;

      if (!node->left && !node->right) {
        res += total;
      }

      if (node->left) {
        st.push({node->left, total});
      }

      if (node->right) {
        st.push({node->right, total});
      }
    }

    return res;
  }
};