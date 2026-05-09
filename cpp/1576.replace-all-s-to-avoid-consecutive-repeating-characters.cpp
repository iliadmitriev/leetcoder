#include <string>
using std::string;

class Solution {
public:
  string modifyString(string s) {
    const int n = s.size();

    for (int i = 0; i < n; i++) {
      if (s[i] != '?') {
        continue;
      }

      char left = i > 0 ? s[i - 1] : 'a';
      char right = i < n - 1 ? s[i + 1] : 'a';

      for (char c = 'a'; c <= 'c'; c++) {
        if (c != left && c != right) {
          s[i] = c;
          break;
        }
      }
    }

    return s;
  }
};