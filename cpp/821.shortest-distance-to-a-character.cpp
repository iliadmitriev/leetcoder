#include <algorithm>
#include <climits>
#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  vector<int> shortestToChar(string s, char c) {
    vector<int> res(s.size(), s.size());

    int pos = s.size();

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == c) {
        pos = i;
      }
      res[i] = abs(i - pos);
    }

    for (int i = s.size() - 1; i >= 0; i--) {
      if (s[i] == c) {
        pos = i;
      }
      res[i] = std::min(res[i], abs(pos - i));
    }

    return res;
  }
};