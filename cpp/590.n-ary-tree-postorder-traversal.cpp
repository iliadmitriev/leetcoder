
class Solution {
private:
  void inorder(Node *node, std::function<void(Node *)> f) {
    if (!node) {
      return;
    }

    std::stack<pair<Node *, bool>> st;
    st.push({node, false});

    while (st.size()) {
      auto [node, visited] = st.top();
      st.pop();

      if (!visited) {
        st.push({node, true});
        for (auto child = node->children.rbegin();
             child != node->children.rend(); child++) {
          st.push({*child, false});
        }
      } else {
        f(node);
      }
    }
  }

public:
  vector<int> postorder(Node *root) {
    vector<int> result;

    inorder(root, [&result](Node *node) { result.push_back(node->val); });
    return result;
  }
};