#include <string>
#include <vector>

using std::string;
using std::vector;

class Solution {
public:
  bool checkDistances(string s, vector<int> &distance) {
    int n = s.size();

    for (int i = 0; i < n; i++) {
      int j = distance[s[i] - 'a'];
      int right = i + j + 1;
      int left = i - j - 1;

      if ((left >= 0 && s[left] == s[i]) || (right < n && s[right] == s[i])) {
        continue;
      }

      return false;
    }

    return true;
  }
};