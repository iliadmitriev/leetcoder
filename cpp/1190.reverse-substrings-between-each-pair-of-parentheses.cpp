#include <string>
#include <utility>
#include <vector>

using std::string;
using std::vector;

class Solution {
private:
  void revStrInd(string &s, int i) {
    int j = s.size() - 1;
    while (i < j) {
      std::swap(s[i++], s[j--]);
    }
  }

public:
  string reverseParentheses(string s) {
    string cur;
    vector<int> st;

    for (char c : s) {
      if (c == '(') {
        st.push_back(cur.size());
      } else if (c == ')') {
        revStrInd(cur, st.back());
        st.pop_back();
      } else {
        cur.push_back(c);
      }
    }

    return cur;
  }
};