
class FindElements {
private:
  unordered_set<int> _set;
  void _recover(TreeNode *node, int val) {
    if (!node) {
      return;
    }

    _set.insert(val);

    _recover(node->left, 2 * val + 1);
    _recover(node->right, 2 * val + 2);
  }

public:
  FindElements(TreeNode *root) { _recover(root, 0); }

  bool find(int target) { return _set.find(target) != _set.end(); }
};
