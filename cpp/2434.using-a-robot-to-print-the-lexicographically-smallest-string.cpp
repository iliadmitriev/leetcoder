#include <array>
#include <stack>
#include <string>

using std::stack, std::string, std::array;

class Solution {
public:
  string robotWithString(string s) {
    stack<char> st;
    array<int, 26> cnt = {0};
    string res;
    res.reserve(s.size());

    // count frequency of characters
    for (char c : s) {
      cnt[c - 'a']++;
    }

    int i = 0;

    for (char c = 'a'; c <= 'z'; c++) {
      while (st.size() && st.top() <= c) {
        res.push_back(st.top());
        st.pop();
      }

      while (cnt[c - 'a'] > 0) {
        if (s[i] == c) {
          res.push_back(s[i]);
        } else {
          st.push(s[i]);
        }

        cnt[s[i] - 'a']--;
        i++;
      }
    }

    while (st.size()) {
      res.push_back(st.top());
      st.pop();
    }

    return res;
  }
};