#include <stack>
#include <string>
using namespace std;

class Solution {
public:
  string minRemoveToMakeValid(string s) {
    stack<int> st;
    string tmp(s.begin(), s.end());

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '(')
        st.push(i);
      else if (s[i] == ')') {
        if (!st.empty() && s[st.top()] == '(')
          st.pop();
        else
          st.push(i);
      }
    }

    while (!st.empty()) {
      tmp[st.top()] = '*';
      st.pop();
    }

    string result;
    result.reserve(tmp.size());

    for (char c : tmp) {
      if (c == '*')
        continue;
      result.push_back(c);
    }

    return result;
  }
};