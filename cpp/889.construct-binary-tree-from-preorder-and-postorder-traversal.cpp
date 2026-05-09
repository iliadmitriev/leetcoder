
class Solution {
public:
  TreeNode *constructFromPrePost(vector<int> &preorder,
                                 vector<int> &postorder) {
    stack<TreeNode *> st;
    TreeNode *node = nullptr;
    const int N = preorder.size();
    int i = 0, j = 0;

    while (j < N) {
      if (!st.empty() && st.top()->val == postorder[j]) {
        node = st.top();
        st.pop();
        j++;
        continue;
      }

      node = new TreeNode(preorder[i++]);
      if (!st.empty()) {
        if (st.top()->left) {
          st.top()->right = node;
        } else {
          st.top()->left = node;
        }
      }

      st.push(node);
    }

    return node;
  }
};