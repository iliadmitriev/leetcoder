
class Solution {
private:
  void revInorder(TreeNode *root, function<void(TreeNode *)> func) {
    stack<tuple<TreeNode *, bool>> q;
    q.push({root, false});

    while (!q.empty()) {
      auto [node, flag] = q.top();
      q.pop();

      if (flag) {
        func(node);
      } else {
        if (node->left) {
          q.push({node->left, false});
        }
        q.push({node, true});
        if (node->right) {
          q.push({node->right, false});
        }
      }
    }
  }

public:
  TreeNode *bstToGst(TreeNode *root) {
    int total = 0;
    revInorder(root, [&total](TreeNode *node) -> void {
      total += node->val;
      node->val = total;
    });

    return root;
  }
};