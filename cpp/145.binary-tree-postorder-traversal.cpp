#include <functional>
#include <vector>

using std::vector;

class Solution {
private:
  void postorder(TreeNode *node, std::function<void(TreeNode *)> f) {
    if (!node) {
      return;
    }

    postorder(node->left, f);
    postorder(node->right, f);
    f(node);
  }

public:
  vector<int> postorderTraversal(TreeNode *root) {
    vector<int> res;

    postorder(root, [&res](TreeNode *node) { res.push_back(node->val); });
    return res;
  }
};