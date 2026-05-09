#include <stack>
#include <string>
using std::stack;
using std::string;

class Solution {
private:
  bool isPalindrome(const string &s, int l, int r) {
    while (l < r) {
      if (s[l] != s[r])
        return false;
      l++, r--;
    }

    return true;
  }

public:
  string shortestPalindrome(string s) {
    if (!s.size()) {
      return s;
    }

    long prefix = 0, suffix = 0;
    long power = 1;
    const long base = 29, mod = int(1e9) + 7;
    stack<int> st;
    int n = s.size();

    for (int i = 0; i < n; i++) {
      int ch = s[i] - 'a' + 1;

      prefix = (prefix * base) % mod;
      prefix = (prefix + ch) % mod;

      suffix = (suffix + ch * power) % mod;
      power = (power * base) % mod;

      if (suffix == prefix) {
        st.push(i);
      }
    }

    while (st.size()) {
      int i = st.top();
      st.pop();
      if (isPalindrome(s, 0, i)) {
        string left = s.substr(i + 1);
        return string(left.rbegin(), left.rend()) + s;
      }
    }

    string left = s.substr(1);
    return string(left.rbegin(), left.rend()) + s;
  }
};