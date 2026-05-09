#include <algorithm>
#include <string>

using std::string;
using std::swap;

class Solution {
public:
  string reverseStr(string s, int k) {
    int n = s.size();
    int m;

    for (int i = 0; i < n; i += (2 * k)) {
      m = std::min(i + k, n);

      for (int j = 0; j < (m - i) / 2; j++) {
        swap(s[i + j], s[m - 1 - j]);
      }
    }

    return s;
  }
};