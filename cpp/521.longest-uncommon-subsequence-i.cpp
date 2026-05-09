#include <string>

using std::string;
class Solution {
public:
  int findLUSlength(string a, string b) {
    return a == b ? -1 : std::max(a.size(), b.size());
  }
};