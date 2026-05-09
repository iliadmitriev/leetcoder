class Solution {
private:
  void inorder(TreeNode *node, function<void(TreeNode *)> func) {
    if (!node) {
      return;
    }
    stack<pair<TreeNode *, bool>> st;
    st.push({node, false});
    while (st.size()) {
      auto [node, done] = st.top();
      st.pop();
      if (done) {
        func(node);
      } else {
        if (node->right) {
          st.push({node->right, false});
        }
        st.push({node, true});
        if (node->left) {
          st.push({node->left, false});
        }
      }
    }
  }

  TreeNode *build(const vector<TreeNode *> &buff, int left, int right) {
    if (left > right) {
      return nullptr;
    }
    int mid = (left + right) / 2;
    TreeNode *node = buff[mid];
    node->left = build(buff, left, mid - 1);
    node->right = build(buff, mid + 1, right);
    return node;
  }

public:
  TreeNode *balanceBST(TreeNode *root) {
    vector<TreeNode *> buff;
    inorder(root, [&buff](TreeNode *node) { buff.push_back(node); });

    return build(buff, 0, buff.size() - 1);
  }
};