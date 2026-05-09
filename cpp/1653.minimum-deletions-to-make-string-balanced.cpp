#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  int minimumDeletions(string s) {
    int n = s.size() + 1;
    vector<int> aSuff(n, 0), bPref(n, 0);

    for (int i = n - 2; i >= 0; --i) {
      aSuff[i] = (s[i] == 'a') + aSuff[i + 1];
    }

    for (int i = 1; i < n; ++i) {
      bPref[i] = (s[i - 1] == 'b') + bPref[i - 1];
    }

    int res = s.size();
    for (int i = 0; i < n; ++i) {
      res = std::min(res, aSuff[i] + bPref[i]);
    }

    return res;
  }
};