
class Solution {

public:
  TreeNode *recoverFromPreorder(string traversal) {
    stack<TreeNode *> st;
    int i = 0;

    while (i < traversal.size()) {
      int level = 0, val = 0;
      while (i < traversal.size() && traversal[i] == '-') {
        i++;
        level++;
      }

      while (i < traversal.size() && std::isdigit(traversal[i])) {
        val = val * 10 + traversal[i] - '0';
        i++;
      }

      while (st.size() > level) {
        st.pop();
      }

      TreeNode *node = new TreeNode(val);

      if (!st.empty()) {
        if (st.top()->left) {
          st.top()->right = node;
        } else {
          st.top()->left = node;
        }
      }

      st.push(node);
    }

    TreeNode *root = nullptr;
    while (!st.empty()) {
      root = st.top();
      st.pop();
    }
    return root;
  }
};