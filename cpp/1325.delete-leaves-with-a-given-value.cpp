
class Solution {
public:
  TreeNode *removeLeafNodes(TreeNode *root, int target) {
    if (!root)
      return nullptr;

    stack<pair<TreeNode *, bool>> st; // stack: node, visited
    st.push({root, false});

    unordered_map<TreeNode *, TreeNode *> ret;

    while (!st.empty()) {
      auto [node, visited] = st.top();
      st.pop();

      if (visited) {
        node->left = ret[node->left];
        node->right = ret[node->right];

        if (node->left == nullptr && node->right == nullptr &&
            node->val == target) {
          ret[node] = nullptr;
        } else {
          ret[node] = node;
        }

        ret.erase(node->left);
        ret.erase(node->right);

      } else {
        st.push({node, true});

        if (node->left)
          st.push({node->left, false});

        if (node->right)
          st.push({node->right, false});
      }
    }

    return ret[root];
  }
};
