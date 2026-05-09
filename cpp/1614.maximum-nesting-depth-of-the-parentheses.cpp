class Solution {
public:
  int maxDepth(string s) {
    stack<char> st;
    int res = 0;

    for (char c : s) {
      if (c == '(') {
        st.push(c);
        res = max(res, (int)st.size());
      } else if (c == ')') {
        st.pop();
      }
    }

    return res;
  }
};