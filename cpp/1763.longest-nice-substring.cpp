#include <set>

class Solution {
public:
    string longestNiceSubstring(string s) {
      set st(s.begin(), s.end());

      for (int i = 0; i < s.size(); i++) {
        char c = s[i];

        if (c >= 'A' && c <= 'Z') {
          c += 32;
        } else {
          c -= 32;
        }

        if (st.find(c) == st.end()) {
          string left = longestNiceSubstring(s.substr(0, i));
          string right = longestNiceSubstring(s.substr(i + 1));

          if (left.size() >= right.size()) {
            return left;
          } else {
            return right;
          }
        }
      }

    
      return s;
    }
};